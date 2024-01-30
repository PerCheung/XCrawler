from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import time
import src.data_processor as data_processor
from src.html.stockutils import getStockTimeUrl
import asyncio

# 页面刷新延时
delay_time = 10


# 获取股票的常用指标数据
def get_common_indicators(soup):
    datas = []
    headers = []
    # 换手率 ，量比，均价等数据
    class_t1 = soup.select_one("div.sider_brief")
    table_t1 = class_t1.find("table")

    index = 0
    for body in table_t1.select("tbody"):
        for tr in body.select("tr"):
            for td in tr.select("td"):
                data = td.get_text()
                arr = data.split("：")
                if index == 0:
                    headers.append(arr[0])
                datas.append(arr[1])
    return headers, datas


# 获取指定股票的分时数据
def get_stock_data(stockNum, driver, url, now, enginstr):
    driver.get(url)
    driver.implicitly_wait(delay_time)
    soup = BeautifulSoup(driver.page_source, "lxml")
    namediv = soup.select_one("div.quote_title_l")
    namespan = namediv.find("span", class_="quote_title_name quote_title_name_190")
    baseName = namespan.get_text()
    name = baseName + "分时"
    # 将stockNum,stockName存储到数据库，以便后续使用
    titles = ["代码", "名称"]
    titles = list(map(str, titles))
    data_processor.SaveStockNameByNum(stockNum, baseName, titles, enginstr, "代码库")
    # 买1-买5，卖1-卖5数据
    class_mm = soup.select_one("div.mm")
    table = class_mm.find("table")

    headers, datas = get_common_indicators(soup)

    index = 0
    # 格式化为字符串
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    date_part, time_part = formatted.split(" ")
    if now.time() >= time(15, 0, 0):
        time_part = "15:00:00"
    for body in table.select("tbody"):
        titleIndex = 0
        for tr in body.select("tr"):
            index = 0
            titleStr = ""
            value = ""
            for td in tr.select("td"):
                data = td.get_text()
                if index == 0 and titleIndex != 5:
                    titleStr = data
                    headers.append(titleStr)
                if index == 1:
                    value = data
                elif index == 2:
                    data = data + "--价位:" + value
                    datas.append(data)
                index = index + 1
            titleIndex = titleIndex + 1
    headers.append("日期")
    headers.append("时间")
    datas.append(date_part)
    datas.append(time_part)
    datas = list(map(str, datas))
    headers = list(map(str, headers))
    #  src.data_processor.SaveToXlsx(datas,headers,f"Assets/{stockNum}_time.xlsx")
    #  src.data_processor.SaveToCsv(datas,headers,f"Assets/{stockNum}_time.csv")
    #  src.data_processor.SaveToJson(datas,f"Assets/{stockNum}_time.json")
    data_processor.SaveTosqlMinutes(datas, headers, enginstr, time_part, name)
    print(f"{name} stockminutesdata crawle completed")


# 循环爬取制定股票分时数据
def getStocksTime(stockNum, now, enginstr):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument('--disable-tabs')
    driver = webdriver.Chrome(options=options)
    url = getStockTimeUrl(stockNum)
    # url = f"http://quote.eastmoney.com/sh{stockNum}.html"
    # while True:
    get_stock_data(stockNum, driver, url, now, enginstr)
    #  time.sleep(10)


async def checkAllTimeStock(stockNum):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument('--disable-tabs')
    driver = webdriver.Chrome(options=options)
    url = getStockTimeUrl(stockNum)
    datas = []
    driver.get(url)
    driver.implicitly_wait(delay_time)
    soup = BeautifulSoup(driver.page_source, "lxml")
    namediv = soup.select_one("div.quote_title_l")
    namespan = namediv.find("span", class_="quote_title_name quote_title_name_190")
    name = namespan.get_text()
    await asyncio.sleep(delay_time)
    headers, datas = await asyncio.to_thread(get_common_indicators, soup)
    return headers, datas, name

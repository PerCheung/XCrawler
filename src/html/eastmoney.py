import src.html
import time
from selenium import webdriver
import datetime
import time
import tushare as ts
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
bashPath = "http://quote.eastmoney.com"
enginstr = "mysql+pymysql://root:Akeboshi123~@localhost:3306/stock"

# ================================ 个人抓取
def get_Data(driver,tmpUrl):
      print("east is runing")
      print(tmpUrl)
      url = driver.get(tmpUrl) 
      driver.implicitly_wait(2)
      soup = src.html.BeautifulSoup(driver.page_source,'lxml')
      # print(driver.page_source)    # 访问东方财富.
      # soup select寻找的方式更加效率
      table = soup.select('table.zjl1')
      logo = soup.select('a.logolink2')
      # soup find all方式寻找效率低些，但基于递归的数据用find_all就比较合适
      # table = soup.find_all('table',class_='zjl1')
      # logo = soup.find_all('a',class_='logolink2')
      # 线上抓图，识图
      for a_tag in logo:
      #    text = a_tag.text  # 获取<a>标签内的文本内容
        href = a_tag['href']  # 获取<a>标签的href属性值
      #    print(f"文本内容: {text}")
        # print(f"链接地址: {href}")
        img_tag = a_tag.find('img')
        if img_tag:
               img_src = img_tag['src']
               img_alt = img_tag['alt']
              #  print(f"图片地址: {img_src}")
              #  print(f"图片描述: {img_alt}")
               img_url = src.html.urljoin(bashPath, img_src)
              #  print(f"原始图片地址: {img_url}")
                # 发送GET请求下载图片
               img_response = src.html.requests.get(img_url)

               # 使用Image.open打开图片
               image = src.html.Image.open(src.html.BytesIO(img_response.content))
               image = image.convert('L')
               # 设置 pytesseract 参数
               custom_config = r'--psm 6 --oem 2'
               text = src.html.pytesseract.image_to_string(image,lang='chi_sim',config=custom_config)
              #  print('picture:'+text)

      datas = []
      
     
    # 线上抓数据
      for ta in table:
    # print(ta.text)
          for body in ta.select('tbody'):
              for tr in body.select('tr'):
               data = tr.get_text()
               datas.append(data)
               print(tr.get_text())
      datas = list(map(str, datas))
       # 写入xlsx title
      datas.insert(0, "数据")
      src.xlsx.SaveToXlsx(datas,"Assets/data.xlsx")
      src.xlsx.SaveToCsv(datas,"Assets/data.csv")
      src.xlsx.SaveToJson(datas,"Assets/data.json")
      return soup

# 循环爬取主版股票
def cycle():
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  # options.add_argument('--disable-tabs')
  driver = webdriver.Chrome(options = options)
  url = "http://quote.eastmoney.com/zs000001.html"
  # http://quote.eastmoney.com/sh603496.html
  while True:
     get_Data(driver,url)
     time.sleep(10)

# 获取指定股票的数据
def get_stock_data(stockNum,driver,url):
    datas = []
    driver.get(url) 
    driver.implicitly_wait(2)
    soup = src.html.BeautifulSoup(driver.page_source,'lxml')
    namediv = soup.select_one('div.quote_title_l')
    namespan =  namediv.find('span', class_="quote_title_name quote_title_name_190")
    class_mm = soup.select_one('div.mm')
    table = class_mm.find('table')
    headers = []
    now = datetime.datetime.now()
     # 格式化为字符串
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    for body in table.select('tbody'):
        titleIndex = 0
        for tr in body.select('tr'):
           index = 0
           titleStr = ""
           for td in tr.select('td'):
              data = td.get_text()
              if index ==0 and titleIndex !=5 :
                 titleStr+=data
              if index == 1:
                 titleStr+=":"+data
                 headers.append(titleStr)
              elif index == 2:
                 datas.append(data)
              index = index + 1
           titleIndex = titleIndex + 1
    headers.append("日期")
    datas.append(formatted)
    datas = list(map(str, datas))
    headers = list(map(str, headers))
    print(headers)
    src.xlsx.SaveToXlsx(datas,headers,f"Assets/{stockNum}_time.xlsx")
    src.xlsx.SaveToCsv(datas,headers,f"Assets/{stockNum}_time.csv")
    src.xlsx.SaveToJson(datas,f"Assets/{stockNum}_time.json")
    src.xlsx.SaveTosqlMinutes(datas,headers,enginstr,"分时")
    print("finished")
  


# 循环爬取制定股票数据
def cycleStocks(stockNum):
   options = webdriver.ChromeOptions()
   options.add_argument('--headless')
   # options.add_argument('--disable-tabs')
   driver = webdriver.Chrome(options = options)
   url = f"http://quote.eastmoney.com/sh{stockNum}.html"
   while True:
       get_stock_data(stockNum,driver,url)
       time.sleep(10)


def get_SHBoard_data(driver,tmpUrl):
     headers = []
     datas = []
     url = driver.get(tmpUrl) 
     driver.implicitly_wait(2)
     soup = src.html.BeautifulSoup(driver.page_source,'lxml')
     table = soup.select("table.table_wrapper-table")
     
     timestamp = datetime.datetime.fromtimestamp(time.time())
     now = datetime.datetime.now()
     # 格式化为字符串
     formatted = now.strftime("%Y-%m-%d")
     for ta in table:
        for body in ta.select('thead'):
           for tr in body.select('tr'):
             for th in tr.select('th'):
                data = th.get_text()
                if len(data) != 0 and data != "加自选":
                    headers.append(data)
                    if data == "市净率":
                        # 给时间表插入时间列
                        name="日期"
                        headers.append("日期")
        max = len(headers)
        for body in ta.select('tbody'):
           for tr in body.select('tr'):
             index = 1
             for td in tr.select('td'):
               data1 = td.get_text()
               if len(data1) != 0:
                  index += 1
                  datas.append(data1)
                  if index == max:
                     datas.append(formatted)               
    
    
     datas = list(map(str, datas))
     headers = list(map(str, headers))
     src.xlsx.SaveToCsv(datas,headers,"Assets/sh_data.csv")
     src.xlsx.SaveToXlsx(datas,headers,"Assets/sh_data.xlsx")
     src.xlsx.SaveToJson(datas,"Assets/sh_data.json")
     
     # 已mysql为例,如果已localhost为host,那port端口一般为3306
     # enginstr = "mysql+pymysql://root:Akeboshi123~@localhost:3306/stock"
     src.xlsx.SaveTosql(datas,headers,enginstr,"stock")
     print("Data crawle completed")
     return soup


# 爬取上证交易所股票 
def cycleSHBoard():
   options = webdriver.ChromeOptions()
   options.add_argument('--headless')
   # options.add_argument('--disable-tabs')
   driver = webdriver.Chrome(options = options)
   url = "http://quote.eastmoney.com/center/gridlist.html#sh_a_board"
   while True:
       get_SHBoard_data(driver,url)
       time.sleep(10)

# ==================================== 第三方
# tushare获取股票数据
def getStockData(stockNum):
   dd = ts.get_hist_data(stockNum) #爬取股票近三年的全部日k信息
   print(dd)
   #dd.applymap('002837'+'.xlsx') #将信息导出到excel表格中

# pandas_datareader通过yahoo获取股票数据
def getStockData_datareader(stockNum):
   yf.pdr_override()
   code = stockNum + '.ss'
   stock = pdr.get_data_yahoo(code,'2023-9-01','2023-11-30')
   stock = stock.round(2) 
   stock.to_csv('Assets/' + code + '.csv')
   stock.to_excel('Assets/' + code + '.xlsx')
   stock.to_json('Assets/' + code + '.json')
   
   # 已mysql为例,如果已localhost为host,那port端口一般为3306
   # enginstr = "mysql+pymysql://root:Akeboshi123~@localhost:3306/stock"
   src.xlsx.ReaderSavetosql(enginstr,"张江高科",stock)
   
   
   # 5日收盘价均价
   mean_price_5 = stock['Close'].rolling(window=5).mean() 
   mean_price_10 = stock['Close'].rolling(window=10).mean() 
   mean_price_20 = stock['Close'].rolling(window=20).mean() 
   mean_price_30 = stock['Close'].rolling(window=30).mean() 
   mean_price_40 = stock['Close'].rolling(window=40).mean() 
   mean_price_60 = stock['Close'].rolling(window=60).mean() 
   # zonghe_data=pd.concat([mean_price_5,mean_price_10,mean_price_20,mean_price_30,mean_price_40,mean_price_60],axis=1)
   # zonghe_data.columns = ['MA5','MA10','MA20','MA30','MA40','MA60']
   # zonghe_data[ ['MA5','MA10','MA20','MA30','MA40','MA60']].plot(subplots=False,style=['r','g','b','m'],grid=True)
   # print(f"MA5: {mean_price_5} MA10: {mean_price_10} MA30: {mean_price_30}")
   # plt.show()

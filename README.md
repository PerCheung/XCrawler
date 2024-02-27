
# XCrawler
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Code-python-blue"></a>
<a href="https://pypi.org/project/PyQt6/"><img src="https://img.shields.io/badge/UI-PyQt6-green"></a>
<a href="https://github.com/Stock-Fund/algorithm/"><img src="https://img.shields.io/badge/Algorithm-algorithm-yellow"></a>
<a href="https://github.com/Stock-Fund/algorithm_server"><img src="https://img.shields.io/badge/Algorithm-Server-pink"></a>
<a href="http://dev.mysql.com/"><img src="https://img.shields.io/badge/Database-MySQL-red.svg?style=flat"></a>

A股爬虫项目
- 环境安装:
  - python3.10.12
  - pip3.10.12
  - chromedriver (需在usr/local/bin 路径下 xattr -d com.apple.quarantine chromedriver添加信任)
  - selenium
  - pandas
  - numpy
  - mysql
  - pycharm
  - Assets文件夹内添加一个本地文件password.txt，内部包含host,user,password,db,分别填入对应内容，(host:数据库地址，user:数据库用户名，password:数据库密码，db:数据库名称)

- 核心逻辑1:通过财经网址获取全部股票的动态数据，并且经过分析，将日涨，日跌超过x%的股票进行筛选，按照股票的涨跌幅进行排序；通过对股票的大额买入卖出订单进行排序，并预测前10位买入卖出的之后的大概股价，并对买入卖出进行排序；并存储到数据库(DB:Mysql，需要跟进)

- 核心逻辑2:对保留到数据库的数据按照5日，20日进行分析排序，筛选出5，20日上涨，下降的前x位的股票，进行排序，并存储到数据库(DB:Mysql)

- 核心逻辑3:做T，通过股票的涨跌幅，对股票进行T操作 (此为量化核心逻辑)
  1. 使用技术指标建模交易信号。比如利用布林通道、均线交叉等技术分析指标,建立买入和卖出规则。
  2. 加入风险管理作为交易决策依据。比如设置止损价格和动态调整仓位,降低单日风险。
  3. 采用复合指标相结合,避免单一依赖某一指标。比如结合MACD、KDJ等多 time frame 的指标信号。
  4. 进行回测优化,找出参数组合效果好的交易策略。优化周期、触发点设定等策略变量。
  5. 采用平滑移动平均线,避免被短期波动误导。比如用EMA作为买入信号。
  6. 重点跟踪行业领跑股票,利用行业势头。同时观察大盘走势变化。
  7. 使用量化选股条件排除个股风险,比如营收同比增长、获利能力等。
  8. 定期回顾回测结果,调整不好的交易规则。持续优化策略模型。
  9. 采取分散投资多个股票池分担风险。

- 核心逻辑4(分时逻辑):
  1. 通过分析分时大额订单(主力)，小额订单(散户)，来分析当前主力参与程度及后市趋势可能

- 核心逻辑5(龙头效用):
  在股市中，龙头股是市场热点的主要来源，是市场情绪的集中体现，是市场资金的“风向标”。板块龙头股的涨跌影响着这个板块后续的趋势，及该板块其他股票的走势

- 核型逻辑6(主升浪逻辑):
  主升浪逻辑在股票技术分析中指的是以下几点:

  1. 趋势连续上涨。价格形成一系列超过坚振位的高点和低点,形成上扬趋势。
  2. 均线上行。成交量均线、动量指标等有力指标呈现上升趋势, signaling价格将继续上涨。
  3. 技术指标佳于基本面。即技术因素如动量等影响较大,价格上行主要由投资者情绪驱动。
  4. 竞争与买盘较强。上涨过程中出现多次触及上轨压力线后重新上扬,反映买方竞争活跃。
  5. 低位集中收购。大买盘在价格收歇低位时出手,下单支持价格逆势上扬。
  6. 新高突破。价格形成一系列 newer highs,创出新的高点,显示主要趋势仍在上行。
  7. 指标穿线支持。如动量指标金叉死叉等技术信号表明趋势有望继续。

- 核心逻辑7:
  A股核心逻辑，政策导向，以上所有逻辑皆基于政策，呵呵

部分参数解释:
- 放量:
  以该股票最近一个月或者三个月的日均交易量为基准平均值。
  如果该日交易量高于基准平均值的一定倍数(如150%或者200%),则认为该日交易量较大,是放量。
- 缩量:
  如果该日交易量低于基准平均值的一定比例(如50%或者70%),则认为该日交易量较小,是缩量。
- 数据拟合:
  拟合(Fitting)指的是使用某种数学函数(通常是多项式函数)来描述一组观察数据的变化趋势或隐含关系。
  - 拟合的目的是从样本数据中提取隐含关系
  - 它寻找一个最优函数来描述观测数据的整体趋势
  - 这样我们就可以用这个函数来预测和理解新数据的预测值

- 龙头股:指在某个行业或板块中，具有较高市值、领先地位和较强盈利能力的公司。龙头股通常在市场上具有较高的知名度和影响力，其股价表现和业绩状况常常被视为该行业或板块整体发展的风向标。
- 中军股:指在某个行业或板块中，位于龙头股之后，具有一定市场份额和较强实力的公司。中军股通常在市场上具有一定的竞争力，股价表现和业绩状况可能对整个行业或板块产生一定的影响。
- 先锋:指在某个行业或板块中，具有创新能力、颠覆性技术或前瞻性战略的公司。先锋公司通常在新兴领域或未来趋势中占据先导地位，其发展可能对整个行业或板块的变革和发展起到重要作用。
- 助攻:在股市中，助攻通常指某只股票的表现受到其他相关股票或市场因素的积极影响，从而推动该股票的价格上涨。助攻可以是来自同一行业或板块的其他股票的利好消息、市场整体的上涨趋势或其他相关因素。
- 卡位:在股市中，卡位通常指通过买入或卖出股票来占据有利的交易位置。卡位者通常会根据市场走势、技术分析或其他因素来选择合适的时机进行买入或卖出，以获取更好的交易执行价格和利润。
- 补涨:在股市中，补涨通常指一只股票在短时间内迅速上涨，而其他相关股票相对滞涨的情况。补涨者可能会寻找滞涨的股票，并预期其在补涨期内追赶上涨趋势，以获取更高的回报。
- 跟风:在股市中，跟风通常指投资者根据某只股票或市场的走势，采取与大多数市场参与者相同的行动。跟风者可能会根据市场热点、投资者情绪或其他因素来追随市场趋势，以期望获取类似的收益。


- 上影线(阳线):当日收盘价高于前一日开盘价,形成的阳线称为上影线。
  多次出现上影线表明价格重重阻力难上,预示进一步上涨势头可能受阻。
  长上影线是多空双方经过剧烈拼杀，多方的上攻意愿较强，空方奋力反击形成的K线
- 下影线(阴线):当日收盘价低于前一日开盘价,形成的阴线称为下影线。
  多次出现下影线表明价格受压难支,预示下跌趋势可能加剧。
  长下影线则是空方向下打压意愿较强，多方奋力反击形成的K线
- 上下影线长度要求是K线实体的2-3倍，才可视为长上影线或长下影线，最标准的形态结构是影线是实体的3倍以上。
- 筹码集中度:筹码集中度，是指某只个股票的筹码集中程度，也就是一只个股的筹码被庄家掌握的程度。
  1. 筹码集中度的计算公式: 筹码集中度=成本区间的（高值-低值）/（高值+低值）。 筹码集中的成本区间越大，集中度的数值越高，筹码越分散；成本区间越小，集中度的数值越低，筹码越集中。
- SMA(MA)(简单平均数)
  - 普通移动平均线(Moving Average):表示求x在n周期内的简单移动平均
  - 计算方法:n个时间单位移动平均线= (第1个时间单位价格+第2时间单位价格+…+第n时间单位价格)/n
  - 5日均线(5 SMA):是指股票在最近5个交易日(不包括当日)内每日收盘价格的平均值。反映近期价格动向。
  - 10日均线(10 SMA):是指股票在最近10个交易日(不包括当日)内每日收盘价格的平均值。较5日均线则反应的周期稍长。
  - 20日均线(20 SMA):是指股票在最近20个交易日(不包括当日)内每日收盘价格的平均值。相对5日和10日均线,20日均线反映了价格动向的中期趋势。
  - 这三条均线使用不同交易日计算平均价格,周期从短到长。
    - 5日判断近期短中长线价格走势
    - 10日金叉与死叉形成买卖信号
    - 20日价格与不同周期均线的交叉位点形成支持 Resistance 轴。

- EMA(指数移动平均线 EXPMA指标)
  - 通俗说法,EMA则需要给每个时间单位的最高最低等价位数值做一个权重处理，然后再平均,对于越近期的收盘价给予更高的权重，也就是说越靠近当天的收盘价对EMA产生的影响力越大，而越远离当天的收盘价则呈现指数式递减。指数平滑移动平均线的初始值计算方法与简单移动平均相同，也就是将n日间的收盘价的合计除以n算出。然后从第2日起，以前一日的EMA+平滑化常数α×（当日收盘价-前日EMA）算出。此外，平滑化常数为α＝2÷（n+1）。使用此平滑化常数计算，比重就会呈现指数函数性的衰减。相对于SMA来说，EMA走势更为平滑，反映较为灵敏，能更即时反应出近期股价涨跌的波动与转折。但也容易在震荡环境下被主力洗筹的假象给洗出去
  - 指数移动平均线指标(Exponential Moving Average):表示求x在n周期内的平滑移动平均。(指数加权)
  - 计算方法:
    当前周期单位指数平均值 = 平滑系数 * (当前周期单位指数值 - 上一个周期单位指数平均值) + 上一个周期单位指数平均值；
    平滑系数= 2 / (周期单位+1)
    得到：EMA(N) = [ (N-1) * EMA(N-1) + 2 * X(当前周期单位的收盘价)] / (N+1)
  - 均线的发散形态:是指短期、中期、长期均线逐渐展开，间距逐渐拉大而形成的扩散运行状态。而从炒股经验的分类上看，发散形态又可以分为多头排列和空头排列。
      1. 多头排列:指均线的向上发散形态，在市场的上升行情中，短期、中期、长期均线由上而下依次排列，并呈发散状向右上方移动。从股票技术分析的角度上看，多头排列形态说明市场做多的力量已经控制了局面，上涨行情或将继续延续,就是说5日线在最上面，其次是10日，再次是30日，以此类推。多头排列表明现在持有这个股票的人几乎都是获利的。多头排列的股票肯定是上涨的
      2. 空头排列:短期均线运行在下，中、长期均线依时间顺序运行在上称均线空头排列，表示市场呈弱势特征,从上到下分别是30日，10日，5日，表明短期的价格低于长期的价格，说明市场趋势向下
- WMA(加权移动平均线)
  - 加权移动平均线指标(Weighted Moving Average):表示求x在n周期内的加权移动平均。在计算平均价格时，对于越近期的收盘价给予越高的权重，而较后期的收盘价则占有较小权重。不过与EMA之间的差异在于，WMA使用的加权乘数是以「线性递减」的方式，与EMA的加权乘数呈现不固定式递减的方式不同。在市场上，WMA这条均线比较少人在使用，绝大多数人还是使用较简单理解的SMA作为主要观察的均线。
  - 计算方法:WMA(N) = [N*第N天收盘价 + (N-1)*第N-1天收盘价 + … + 1*第1天收盘价] / (N+N-1+N-2+....+1)加权乘数总和

- 复权与不复权的一些概念
  - 复权
    1. 就是股票原价,不做任何修正
    2. 随着股票拆分、 dividends 等因素,价格会出现断点。
    3. 不同期间价格不易直接比较。
  - 不复权
    1. 对股票价格进行修正,消除分红、送股等影响。
    2. 通过调整计算出如未出现分红等影响的理论价格。
    3. 使不同时期价格具有直接比价性。
  - 区别:总的来说不复权价格反映实际变动,但时间上不连续;
        复权价格适用于趋势分析,抹平非基本因素影响,利于长线研判。

- KDJ指标
  - KDJ指标的含义：KDJ是一个动量指标,用于衡量股票近期价格动能的强弱,并判断趋势形成的信号。
  - K值(K)
    1. 衡量最近买势与卖势的相对强度,范围0-100。
    2. K=(C-L14)/(H14-L14)*100
       - C:最近一日收盘价
       - L14:最近14日最低价
       - H14:最近14日最高价

  - D值(D)
    1. K值的简单移动平均,平滑K值的波动。
    2. 当日D = 前一日D值 × (1 - a) + 当日K值 × a (一般a取0.2)

  - J值(J)
    1. 衡量K值与D值距离的平均值,判断K线与D线背离程度。
    2. 当日J = (当日K+前一日K+前一日D)⁄3

  - 指标意义:
    1. K>D表示空头势头较弱或已转弱
    2. K<D表示多头势头较强
    3. K线上穿或下破D线,即K与D背离,可以看作趋势结束或变化的信号

- 布林线指标(Bollinger Bands)
  - 布林线指标是John Bollinger在1986年提出的一种易用且有效的趋势通道指标。是由中轨线和上轨线和下轨线组成。一般可与kdj指标同时分析,得出金叉(起飞信号),死叉(下降信号)信息

  - 布林线指标计算公式:
    - 上轨:20日均线+2倍标准差
    - 中轨:20日均线
    - 下轨:20日均线-2倍标准差
    - 标准差:标准差可以反映一个数据集的离散程度
      - 标准差公式:Σ(收盘价-MA(N日平均线))2/N [N日所有收盘价-N日平均线 所得差开平方的总和 再除以N 得到的结果开根号]
      eg:则:
      Σ(收盘价-MA)2 = (10-15)2 + (11-15)2 + ...+(28-15)2
      Σ(收盘价-MA)2 / 20 = 和/20
      标准差 = √和/20

  - 布林线指标意义:
    1. 由一条20日均线和标准差线组成上下界形成的通道。
    2. 标准差线一般取2倍标准差,表示价格波动98%时间范围内的上下波动空间。
    3. 当价格上行突破上轨或下跌破下轨,反映趋势可能将要改变。
    4. 中轨即20日均线,可以观察价格与均线的关系来判断多空趋势。
    5. 通道越窄,表明价格波动趋于平稳;越宽,则波动动较大。
    6. 价格带来回于通道内,反映短期震荡趋势;一直保持在通道内表现强势趋势。
    7. 常用在趋势判断、震荡发现、买入点挖掘、止损点确定等多种交易策略中。
  - 布林线指标应用:
    - 喇叭口研判:https://www.zhihu.com/question/384284854
      1. 开口型:开口型喇叭口预示着一方力量逐渐强大而一方力量逐步衰竭，价格将处于短期单向行情中，方向则一般由盘整时所处的位置决定，例如高位盘整开口一般意味着暴跌，低位盘整则一般意味着暴涨.
      样子类似喇叭
      开口型喇叭口形态的形成必须具备两个条件。
      其一，长时间的横盘整理，整理时间越长、上下轨之间的距离越小则未来波动的幅度越大；
      其二，布林线开口时要有明显的大的成交量出现。
      开口喇叭口形态的确立是以K线向上突破上轨线、价格带量向上突破中长期均线为准
      2. 收口型:经历上涨后收口型喇叭口预示着空头力量逐渐强大而多头力量开始衰竭，价格将处于短期大幅下跌的行情之中。经历下跌后的收口型喇叭口则相反。收口型喇叭口形态的形成虽然对成交量没有要求。
      样子类似反向喇叭
      收口型喇叭具备一个条件，即价格经过前期大幅的短线拉升，拉升的幅度越大、上下轨之间的距离越大则未来下跌幅度越大。上涨后收口型喇叭口形态的确立是以价格的上轨线开始掉头向下、价格向下跌破短期均线为准。
      3. 紧口型:紧口型喇叭口预示着多空双方的力量逐步处于平衡，价格将处于长期横盘整理的行情中,样子类似3条平行线
      紧口型喇叭口形态的形成条件和确认标准比较宽松，只要价格经过较长时间的大幅波动后，成交极度萎缩，上下轨之间的距离越来越小的时候就可认定紧口型喇叭初步形成。当紧口型喇叭口出现后，投资者既可以观望等待，也可以少量建仓。BOLL线还可以配合判断M头和W底，以W底为例，主要是看左底和右底在布林线中处于何种相对位置上。一般来说，W底的左底会触及下轨线甚至跌破下轨线，但右底却大多是收在布林线下轨线之内，跌破下轨线的时候较少。当价格第一次下跌时，价格跌破布林线下轨线，但随后的反弹却比较强劲，价格不仅越过了布林线的中轨，且能上摸至上轨线；当价格第二次下跌时，没有跌破布林线的下轨线，而是与下轨线有一小段距离，受到下轨线的有力支撑，并再次出现了强劲反弹。从二次下探过程中，我们看到，价格的每次下探是逐步与布林线下轨线拉开距离的，这表明布林线显示市场人气在逐渐地增强，在酝酿着转机。

- RSI指标(相对强弱指数)(动能策略)

  - 指标含义:衡量价格上涨或者下跌动能的技术指标
  - 计算公式:RSI＝[上升平均数÷(上升平均数＋下跌平均数)]×100
    - 上升平均数:N日价格的上涨平均数
    - 下跌平均数:N日价格的下跌平均数
  - 应用:RSI最基本的用法是在指标自下而上突破30点时寻找买入，或者在指标自上而下跌破70时卖出。 该策略是押注市场行情会在强弱间切换，当趋势过强时去捕捉向下的转折点，而当趋势太弱时定位向上的突破机会

- OBV能量潮指标
  - 指标含义:OBV能量潮OBV又称为平衡交易量,它的计算方法是人为的按照股价涨跌赋予成交量为正负数,并进行累加操作,其计算得出的数值并没有什么实际意义,但是其趋势方向的变化却很关键,其和K线形态结合起来运用就更加准确,所以OBV是一个不错的猎庄工具,其变动的方向是重要的参考指标.
  - 计算公式: OBV ＝ 前一日OBV+今日成交量 （如果当日收盘价高于前日收盘价取正值，反之取负值，平盘取零！！！）
  - 指标应用
     1. 股价上升而OBV线下降,表示买盘无力,股价可能会回跌
     2. 股价下降而OBV线上升,表示买盘旺盛,逢低接手强股,股价可能会止跌回升.
     3. OBV线缓慢上升,表示买气逐渐加强,为买进信号
     4. OBV线急速上升,表示力量将用尽为卖出信号
     5. OBV线从正的累加数转为负数,为下跌趋势,投资者应该卖出持有股票.反之OBV线从负的累加数转为正数,应买进股票
     6. OBV线最大的用处,在于观察股价横盘整理后,何时会脱离盘整,以及突破后的未来走势.
     7. OBV线对双重顶第二个高峰的确定有较为标准的显示,当股价自双重顶第一个高峰下跌又再次回升时,如果OBV线能够随股价同步上升且价量配合,则可持续多头市场并出现更高峰.相反当股价再次回升时,OBV线未能同步配合,却见下降,则可能形成第二个顶峰,完成双重顶的形态,导致股价反转下跌.即OBV顶背离.
  - 指标缺陷
     1. OBV指标是建立在国外成熟市场上的经验总结,把它移植到国内必然要经过一番改造才行！比如价涨量增,用在A股坐庄的股票上就不灵了.这时股价涨得越高,成交量反而越小.这是因为主力控盘较重,股价在上涨过程中没有获利筹码加以兑现,所以此时股票涨得很疯,但成交量并不增加.OBV自然无法发挥作用.
     2. 另外,涨跌停板的股票也会导致指标失真.由于A股采用涨跌停板的限制,很多股票在连续涨停的时候,由于股民预期后市会继续大涨,往往持股观望,导致出现越长越无量的现象,因为对于那些达到涨跌停板股票,OBV也无法正常发挥作用.
     3. 目前,A股中仍有大量的"坐庄"现象存在,对于中长线庄家而言,需要在股价处于底部的时候尽可能的吸进大量筹码,然后拉到高处派发.在底部收集筹码阶段,必然会由于庄家的买进造成一定的上涨,同时伴随成交量放大,这时候,为了降低吸筹成本,庄家会把小幅上涨的股价向下打压,到底部后继续吸筹.如此反复,直到吸到足够的筹码为止.
     这个过程反映在OBV上,就是股价在底部盘整,而OBV却一波一波走高,形成底部背离形态,需要特别注意的是,大众所掌握的分析方法也有可能被机构利用.就OBV而言,庄家可以在每日盘中吸筹,使成交量增加,收盘时再把股价打成阴线,这样OBV就会往下走,以此来迷惑投资者.要破解这种手段,一个最有效的方法就是选择15分钟或60分钟的OBV线,这样就可以避开庄家释放的烟雾.
     4. OBV用于研判上升趋势,还是不错的,只是在股价进入下降通道之后,OBV一般作为横盘或上升趋势减缓的参考依据.
  - 指标精华
     1. OBV中有很多精华所在,在实战操盘中,可以撇开Y轴的数值不看,仅按其数值所占Y轴比例分为20%,40%,60%,80%,100%五个区域,通常,在大牛市或熊市中,选择半年以上的时间为横坐标X,在箱体整理的行情中侧选择1个月至3个月的时间为横坐标X来观察OBV曲线
     2. OBV线的底背离现象和异常动向,往往对于黑马有着相当明确的指示作用.比如当股价经过大幅的下跌后,OBV值在0~20%的区域内明显止跌回稳,并出现超过一个月以上,近似水平的横向移动时,表面市场正处在一个漫长的盘整期,大部分投资者没有耐心而纷纷离场,然而此时往往预示着做空的能量已慢慢的减少,逢低吸纳的资金已逐渐增强,大行情随时都有可能发生.当OBV值能够有效的向上爬升时,则表明主力收集阶段已经完成,投资者可根据该收集阶段的股价来计算主力吸货阶段的成本价,计算方法为:
     主力成本价=吸货区域的(最高价+最低价)/2
     3. 当OBV指标创新高的时候股价并没有新高,这说明OBV和股价已经走在出背离的走势,在这种情况下,往往后期股价会跟随指标创出新高,但这种背离的情况也要符合多个条件
       - 首先,指标突破的时候,成交量是逐渐放大的,但是股价并没有突破平台高点
       - 其次,股价必须处于低位状态,如果涨得特别高,即使背离恐怕利润也不会太多,所以低位放量必须是最基本的条件.
     4. 用OBV指标做到长期持有股票，最简单的办法就是当OBV线保持在OBVMA(OBV均线)之上是进行持股。利用这种方法,大家可能会拿到一整波行情,虽然OBV会拐头向下,但是不跌破OBV均线就说明依然保持强势区域.
- 马科维茨模型
- MACD策略(Moving Average Convergence Divergence 移动平均线收敛与发散策略)
  - MACD指标含义:通过计算较长时间和较短时间指数移动平均线的差异,来衡量股票近期价格动能的强弱。一般可与kdj指标同时分析,得出金叉(起飞信号),死叉(下降信号)信息
  - MACD指标计算公式:MACD＝(ema12- ema26) / (ema12 + ema26) * 200 + ema12 其中ema12为12日指数移动平均线,ema26为26日指数移动平均线
  
- 均线策略
  - 策略含义:均线策略指根据移动平均线的交叉信号进行买入卖出操作。
  - 策略类型:
    1. 金叉死叉策略
       当短期均线(如5/10日均线)从下方突破长期均线(如20/50/200日均线)形成金叉形态,视为买信号;
       当短期均线从上方下穿长期均线形成死叉形态,视为卖信号。

    2. 双均线策略
       比如利用5日均线和20日均线,当5日均线从下方突破20日均线时买入,5日均线从上方下穿20日均线时卖出。

    3. 三均线策略
       利用3条不同周期(如5、10、20日)均线进行买卖决策。
    4.均线斜率利用比如5日线、10日线和20日线等不同时间周期的移动平均线,计算出它们在一定期间内的斜率大小。
       - 斜率越大,表示该时期内价格变动幅度越大,价格变化越剧烈。
       - 斜率正数表示上涨趋势,值趋大说明上涨动力增强;斜率负数表示下跌趋势,值越小表明下跌动能减弱。
       - 不同周期均线斜率可互相对比,如短期均线斜率大于长期均线,预示短期动向向上等。
       - 一般使用5日线和20日线比对,5日线斜率大于0且大于20日线,或5日线转正而20日线维持平稳,预示短期内价格有可能走高
       - 可以绘制成柱状图展示不同周期均线斜率高低关系,跟踪趋势变化
- WR(动量策略)
  - 策略含义:WR指标是衡量市场动量的技术指标。WR指标由Williams %R指标和动量指标(MOM)构成。
    1. 该指标能及早发现行情的转向信号，对突发事件反应灵敏，是短线操作应用指标。在使用过程中，最好能结合强弱指数，动向指数等较为平衡的技术指标一起研制，由此可对行情趋势得出较准确的判断。
    2. 超买、超卖和买卖信号非常清楚，能使投资者了解；发出的超卖信号不等于可以买进，而是告知投资者在此价位不要盲目追卖。反之，发出的超买信号也不等于可以卖出，而是警告投资者不要盲目在此价位追买。
    3. 改变W%R曲线的取样天数可以滤除短线频繁的交叉点买卖信号。
    4. 在使用该指标时，会出现超买之后又超买，超卖之后又超卖现象，常使投资者左右为难，不知如何是好。
  - 计算公式: (N周期内最高价-当前价)/(N周期内最高价-N周期内最低价)*100 其中N一般为4或14。
    取值范围为0-100:
    WR值越大,当前价格距离周期最高价越近,表明动能较强;
    WR值越小,当前价格距离周期最低价越近,表明动能较弱。
  - 判断条件
    1、当威廉指标在20——0区间内时，是指标提示的超买区，表明市场处于超买状态，可考虑卖出。威廉指标20线，一般看做卖出线。
    2、当威廉指标进入80——100区间内时，是指标提示的超卖区，表明市场处于超卖状态，可考虑买入。威廉指标80线，一般看做买入线。
    3、当威廉指标在20——80区间内时，表明市场上多空双方处于相持阶段，价格处于横盘整理，可考虑观望。
  - 总结:威廉指标可以运用于行情的各个周期的研究判断，大体而言，威廉指标可分为5分钟、15分钟、30分钟、60分钟、日、周、月、年等各种周期，
WR连续几次撞顶（底），局部形成双重或多重顶（底），是卖出（买进）的信号。这样的信号更为可靠

- DMI(动能策略)
  - 策略含义:DMI指标又叫动向指标或趋向指标,其全称叫“Directional Movement Index,简称DMI”,也是由美国技术分析大师威尔斯．威尔德（Wells Wilder）所创造的,是一种中长期股市技术分析方法。
    1. 上升方向线+DI(又称PDI), +DI为黄色线
    2. 下降方向线- DI (又称 MDI), -DI为红色线
    3. 趋向平均值ADX，主要用于对趋势的判断, ADX为蓝色线
    4. ADXR，对ADX 的评估数值，也是对市场的评估指标, ADXR为绿色线
  - 策略原理:DMI指标是通过分析股价在涨跌过程中买卖双方力量均衡点的变化情况,即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程,从而提供对趋势判断依据的一种。
　　DMI指标的基本原理是在于寻找股价涨跌过程中,股价藉以创新高价或新低价的功能,研判多空力量,进而寻求买卖双方的均衡点及股价在双方互动下波动的循环过程。在大多数指标中,绝大部分都是以每一日的收盘价的走势及涨跌幅的累计数来计算出不同的分析数据,其不足之处在于忽略了每一日的高低之间的波动幅度。比如某个股票的两日收盘价可能是一样的,但其中一天上下波动的幅度不大,而另一天股价的震幅却在10%以上,那么这两日的行情走势的分析意义决然不同,这点在其他大多数指标中很难表现出来。而DMI指标则是把每日的高低波动的幅度因素计算在内,从而更加准确的反应行情的走势及更好的预测行情未来的发展变化。
  - 计算正向动量指标DI+: DI+ = (当日高点 - 上一日高点)/当日移动范围 × 100
  - 计算负向动量指标DI-: DI- = (当日低点 - 上一日低点)/当日移动范围 × 100
  - 移动范围: 每日最高价 - 每日最低价 移动范围是用来标准化DI+和DI-的值,消除因价格范围不同而引起的指标计算误差
  - 计算动向指标DM: DM+ = DI+的N日简单移动平均  DM- = DI-的N日简单移动平均
  - 计算动向趋势线DX: DX = abs(DM+)/ (abs(DM+)+abs(DM-)) * 100
  - 计算动向移动平均指数DMI: DMI = N日EMA(DX)
  - 计算公式:
  - 参考逻辑:
    1. 多空指标包括(+DI多方、-DI空方 +DM多动向、-DM空动向)
       - +DI在-DI上方,股票行情以上涨为主
       - +DI在-DI下方，股票行情以下跌为主
       - 在股票价格上涨行情中，当+DI向上交叉-DI，是买进信号，相反,当+DI向下交叉-DI，是卖出信号。
       - -DI从20以下上升到50以上,股票价格很有可能会有一波中级下跌行情。
       - +DI从20以下上升到50以上,股票价格很有可能会有一波中级上涨行情。
       - +DI和-DI以20为基准线上下波动时，该股票多空双方拉锯战,股票价格以箱体整理为主。
       - 当ADX脱离20－30之间上行，不论当时的行情是上涨或下跌，都预示股价将在一段时间维持原先的走势。
       - 当ADX位于＋DI与－DI下方，特别是在20之下时，表示股价已经陷入泥沼，应远离观望
       - 当绿色的ADXR曲线低于20时，所有指标都将失去作用，应果断离市。
       - 在一般的行情中，ADX的值高于50以上时，突然改变原来的上升态势调头向下，无论股价正在上涨还是下跌都代表行情即将发生反转。此后ADX往往会持续下降到20左右才会走平。但在极强的上涨行情中ADX在50以上发生向下转折，仅仅下降到40－60之间，随即再度回头上升，在此期间，股价并未下跌而是走出横盘整理的态势。随着ADX再度回升股价向上猛涨，这种现象称为"半空中转折"。也是大行情即将来临的征兆。但在实际操作中仍遵循ADX高于50以上发生向下转折，即抛出持股离场观望，在确认"半空中转折"成立后再跟进的原则
       - 当＋DI与-DI相交之后，ADX会随后与ADXR交叉，此时如果行情上涨，将是最后一次买入机会；如果行情下跌，将是最后一次卖出机会。如图所示，白色的+DI上穿黄色的-DI之后不久，紫色的ADX就上穿绿色的ADXR，随即股价开始大幅上扬。
    2. DMI数值 reflects当前趋势的强弱,通常:
       - DMI>50表示趋势明确
       - 两条DM交叉时可能发生趋势转向
    3. 当四条线由粘连变成分散,并且白线再上,黄线在下,形成张开嘴巴形状时，加关注;
       买点是紫线上穿绿线时
       卖点是白线下穿绿线时。

- 可转债策略
  - 可转债是一种可以在特定的时间、按特定的转换条件转换为标的股票的公司债券，其本质上就是一个债券+看涨期权的组合。因而，可转债的风险低于股票，高于普通债券。可转债之所以受到中低风险投资者的追捧，是因为其兼具股性与债性，进可攻退可守，安全性较高。另一方面，根据风险与收益率相匹配的原则，可转债的收益率低于股票，但高于普通债券。你不能指望既保本，收益率又高于排名靠前的股票基金。
  - 可转移债的影响:
     1. 股价波动。到期日前后,持有人可能根据股价走势决定是否转换为股票,这会带来一定程度的股价波动。

     2. 股本结构变化。如果部分或全部债券转换为股票,公司股本将相应增加,每股收益可能略有下降。

     3. 普通股增发供应。大批量转换将增加额外股份供应,短期内可能会形成一定的卖压。

     4. 股东基础扩大。通过可转债公司增强了股东群体,并获得新的长期股东支持。

     5. 资金来源渠道变多。可转债到期后公司将获得债券发行所得资金,对其进一步发展有帮助。

     6. 市场关注度升高。到期日通常股价波动大,也将吸引更多投资者重点关注该股票。

     7. 融资成本下降。通过可转债公司可降低融资成本,提升资金利用率,对后期经营有利
  - 操作
     1. 股票价格上涨时转换:
        - 可以按较低的转换价格参与公司更高价值。
        - 但此时股价可能会因为供应增加而下跌。
     2. 股票价格下跌时转换:
        - 可以利用低价入市股票
        - 但如果股价继续下跌,将承受更大亏损。
     3. 一般来说
        - 转换价格高于股票价格时,转换成本较高。
        - 当转入大量股票后,会增加股票的流通数量，引起股东结构和控股比例的调整,带来风险
        - 如果市场上可转债过多,会对股票带来一定抛售压力
- 资金流策略
  - 策略含义:资金流策略是指根据标的资产(如股票、期货等)的资金流量变化情况,来进行交易和投资的一种策略。
  - 资金流策略的核心思想是:
   1. 资金流入标的资产代表更多资金参与购买,表明价格或会上涨。

   2. 资金流出标的资产代表更多资金参与卖出,表明价格或会下跌。

  - 资金流策略通常包括:

   1. 量化方式了解和跟踪标的资产的日/周/月等各阶段的净资金流入流出额。

   2. 当资金流入超过流出,代表背书价格上涨,可以买入持有。

   3. 当资金流出超过流入,代表背书价格下跌,可以卖出或空头。

   4. 按周期轮动进行交易,参考资金流量的长短期变化趋势确定买卖时点。也可结合其他技术指标一起研判,例如RSI助长资金流变化判断时点。重点标的包括股票、期货、基金等可以获得详细的日资金流数据。

  - 所以说,资金流策略利用资金行为分析价格走势,寻找买入点空头点,从而获利。
- 换手率逻辑
  - 换手率是衡量股票活跃程度的指标,换手率越大,表明股票成交活跃,股价波动也越大。当换手率下降，成交量下降，股东数下降，个人持股上升时，可能存在阶段性行情
- 量化学习
  - 学习平台:聚宽,掘金,米框,优矿,万矿
- rsrs算法
  - 算法含义:阻力支撑相对强度(Resistance Support Relative Strength, RSRS)是另一种阻力位与支撑位的运用方式，它不再把阻力位与支撑位当做一个定值，而是看做一个变量，反应了交易者对目前市场状态顶底的一种预期判断。
  - RSrs算法的核心逻辑和公式是:
    1. 首先计算一定时间窗口(如14天)内的日收益率:
       日收益率 = (当日收盘价 - 昨日收盘价) / 昨日收盘价
    2. 计算股指或者行业指数在同一时间窗口内的日收益率
    3. 计算个股日收益率与股指日收益率的比值,并取移动平均:
       RS = 个股日收益率 / 股指日收益率
    4. 对所有RS值取n天(如14天)滑动平均,即为RSrs值
       公式: RSrs = (当日RS + 昨日RS + ... + n天前RS) / n
    5. 当RSrs大于等于50,表明个股强于股票指数,预示后期走强;
       当RSrs小于50,表明个股弱于指数,预示后期走弱。
  - Rsrs线斜率:RS线斜率代表趋势变化速度和动能强度,斜率越高代表趋势改变的速度越快，变化幅度越大，趋势的快速改变意味着动能消耗较大，难以维持,前后转换难度也越大,等于趋势面临的阻力越大
  - 斜率(m = y/x 可以通过斜率的正负来判断相对于前一天,当前天价位的涨跌)
    1. 直线斜率正负判断：用右手在线条下端向右侧划线，组成的角度为锐角的，斜率为正，角度为钝角的，斜率为负。
    2. 曲线斜率正负判断：曲线上点的切线所在直线的斜率为k。k＞0，斜率为正；k＜0，斜率为负。
- 乖离率，当k线远离20日生命线大概150点左右会存在反弹趋势，乖离率的大小可以提供关于价格相对于移动平均线的偏离程度的信息。乖离率的绝对值越大，表示价格与移动平均线之间的偏离程度越大。
  - 当乖离率为正值时，表示当前价格高于移动平均线，这可能暗示着价格处于上涨趋势或过度买入的状态。较大的正乖离率可能意味着市场过热或超买的情况。
  - 当乖离率为负值时，表示当前价格低于移动平均线，这可能暗示着价格处于下跌趋势或过度卖出的状态。较大的负乖离率可能意味着市场过冷或超卖的情况。
  - 乖离率的大小和方向可以用来判断价格的超买和超卖情况。当乖离率达到极端值时，可能意味着市场即将出现反转或调整的机会。例如，当正乖离率达到较高水平时，可能暗示着市场上涨趋势即将结束或转为下跌趋势。相反，当负乖离率达到较低水平时，可能暗示着市场下跌趋势即将结束或转为上涨趋势。
  - 需要注意的是，乖离率的大小并不能单独确定价格的未来走势，而是作为其他技术指标和分析方法的辅助工具来使用。交易者应结合其他市场分析工具和自己的判断，综合考虑市场的各种因素，以做出更准确的交易决策。
  - 乖离率的计算方法通常涉及以下步骤：
    选择一个移动平均线作为参考，通常使用简单移动平均线（SMA）或指数移动平均线（EMA）。
    计算移动平均线的值。
    计算当前价格与移动平均线之间的偏离程度。一般是通过以下公式计算乖离率：
     N日乖离率＝( 当日收盘价-N日移动平均价)/ N日移动平均价×100%
  - 在弱势市场中，当股价的N日乖离率达到5以上时，表示超买现象出现，此时可以考虑卖出；当N日乖离率达到-5时，则表示超卖现象出现，可以考虑买入
  - 而当股票处在强势市场时，乖离率达到10以上时表示为超买现象，可以考虑卖出股票；反之达到-10时，表示为超卖现象，可以考虑买入股票
  - 一般短期乖离率偏离值大概在±2%之间，中期在±3%，长期在±5%之间，但这个值因时，因股票而异，需要根据个人的经验判断。
- 融资
  - 融资买入: 投资者通过融资买入方式，向证券公司申请买入证券，融资公司根据投资者申请，划拨证券资产给投资者(做多)
- 融券
  - 融券卖出: 投资者通过融券卖出方式，向证券公司申请卖出证券，融资公司根据投资者申请，划拨证券资产给投资者(做空)
- 爆仓: 融资融券交易中，爆仓通常是在透支投资后，亏损额超过了自有资金。一般在达到强制平仓线时，券商会强制给用户平仓，以保护券商借出的这部分资产
- 平仓线: 融资融券交易中最低维持担保比例平仓线，。维持担保比例=（现金+信用证券账户内证券市值总和）/（融资买入金额+融券卖出证券数量×当前市价+利息及费用总和）。一般券商允许这个比例最高是200%，也就是50万元最多融资融券100万元
- 警戒线: 融资融券交易中最低维持担保比例平仓线+10%
- 补仓线: 融资融券交易中最低维持担保比例平仓线+20%
- 画线逻辑
  - 画线逻辑:前期最低点为起点画线到后期高点为终点画上箱体线其延升线为止盈线；前期低点为起点画线到当日最低点为终点画下箱体线其延升线为止损线；
  - 天量(巨量)之后，存在回调，在柱形图上以天量柱形图的一半做压力位，第二天超过压力位或者超过5日线，就要抛货;如果放量，但量能没有超过均值或前值的一半，则已当前巨量的最低价为防守位
  - 所有的反弹都是从不创新低开始，防守线战法(最高阳线最低价不破，即可持有)
  - 高位跌破5日线，可以先高抛丢一把，等到了20日线/通道下限接回来；如果高位破了20日线，就全丢
  - 一波强势波段-建仓过程
  - 整体调整幅度要小- +10～-2，-3，-5之间，基本上不跌破前高的低位
  - 巨量阴线，如果换手小(抵抗小)，容易拉升
  - 月线红色，周线红色，日线表示进入红色通道(上涨通道)，且当macd线上穿0轴，表示可以入场
  - 通讯设备,it设备
  - 前一天下影线，第二天如果没有往上开，则会用一个实体k线去填补前一天的下影线位置，是为了让这部分空头资金跑完
  - 尾盘拉涨停说明多头较弱，拉尾盘涨停，第二天多数低开
  - 近期反弹多次发生反弹强K线(反包/反包一半  阳线成交量也要放大)，这里就会出现反弹趋势
  - 上升通道中，量价背离是，用前一日的最底线做警戒线，向下跌破则出一半，反之则持有
  - 下降通道中，出现放量反包，则可以轻仓试水
  - 上升通道如果想要介入，可以找阴线部分买入
- 上涨期间短期逻辑
  - 放量，反包，5日线拐头向上(上车三要素)
  - 收盘价不破5日线，不动仓位；短期下穿5日线可以调整仓位(普通操作)/短期破前日k线柱状体一般位置，可调整仓位(保守操作)
  - 成交量呈红色堆量可以考虑买入建仓，当然如果大单净量呈正，且为堆量可放心买入
  

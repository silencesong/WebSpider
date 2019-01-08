# WebSpider
web spider by python

Project1.百度贴吧图片爬取
===========================
* 目标
  * 1.根据用户指定的贴吧名称和起止页，爬取图片
  * 2.将图片保存到本地
* 技术点：
  * 1.使用爬虫模块requests
  * 2.使用xpath进行信息提取

Project2.猫眼电影数据抓取
===========================
* 目标
  * 1.抓取猫眼电影的相关数据
  * 2.将提取信息进行持久化存储
* 技术点：
  * 1.使用爬虫模块urllib.request
  * 2.使用re正则表达式进行信息提取
  * 3.使用csv模块将提取信息存入csv文件
  * 4.将提取信息存入MONGODB数据库进行持久化存储
  * 5.将提取信息存入MYSQL数据库进行持久化存储

Project3.糗事百科笑话抓取
===========================
* 目标
  * 1.抓取糗事百科中段子的作者，内容，好笑数，好评数
  * 2.存入数据库
* 技术点：
  * 1.使用爬虫模块requests
  * 2.使用xpath对相关信息进行解析
  * 3.将提取内容存入MongoDB数据库
  
Project4.豆瓣电影排行榜抓取
===========================
* 目标
  * 1.根据用户的输入，抓取豆瓣电影排行榜中的电影名称及评分
  * 2.存入数据库
* 技术点：
  * 1.对Ajax动态加载的网站数据抓取
  * 2.鼠标滑轮时加载信息，使用Fiddler抓包工具进行抓包
  * 3.分析请求的url地址以及参数
  * 4.将json格式的字符串转换成python数据类型，并提取相关内容
  * 5.保存进Mysql数据库

Project5.京东商品信息爬取
===========================
* 目标
  * 1.根据用户输入的商品名称，抓取京东所有商品的信息(商品的名称,商品的价格,评论的数量,商家的名称)
  * 2.将数据存入到json文件中
* 技术点：
  * 1.使用selenium+chrome模拟登录京东首页，输入商品名称，发送文字，模拟点击，进入商品菜单页面，下拉鼠标，点击下一页等操作
  * 2.对每一页中的所有商品进行相关信息提取
  * 3.浏览器对象的单元素，多元素查找
  * 4.浏览器对象执行js脚本
  * 5.存入json文件
  * 6.也可以设置selenium+phantomjs，可得到同样效果

Project6.链家二手房信息爬取
===========================
* 目标
  * 1.爬取链家二手房网站相关的信息(小区名称，户型，面积，价格等信息)
  * 2.将数据存入到mongodb数据库
* 技术点：
  * 1.使用爬虫模块requests
  * 2.找到url地址变化的规律
  * 3.使用BeautifulSoup对响应中的相关信息进行解析
  * 4.将提取内容存入MongoDB数据库

Project7.斗鱼直播信息抓取
===========================
* 目标
  * 1.爬取斗鱼直播网站中每个视频的主播和热度
  * 2.将数据存入到csv文件
* 技术点：
  * 1.使用selenium+chrome处理JS分页加载的网页
  * 2.模拟点击下一页
  * 3.对每页数据通过xpath进行提取
  * 4.将得到的数据存入csv文件



  

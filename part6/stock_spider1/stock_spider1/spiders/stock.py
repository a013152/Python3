# -*- coding: utf-8 -*-
import scrapy
import re
from urllib import parse
from stock_spider1.items import StockItem

'''生成方式 
    1、在cmd 里 cd 到目录（前提安装好scrapy )
    2、输入  scrapy genspider stock pycs.greedyai.com/   
    3、使用pyCharm 打开文件
    
    4、在Terminal 终端 输入 scrapy shell http://pycs.greedyai.com/ 调试
    
    5、 查看网页源码分析元素 获取到xpath，在终端输入   response.xpath("//a/@href").extract()
    
    6、导入parse包，实现域名拼接
    
    7、在item.py 增加StockItem类， 定义变量保存“姓名、年龄、……"
    
    8、在StockSpider本类parse_detail函数增加StockItem变量，用于保存数据，最后yield 变量stock_item
    
    9、在pipelines.py增加StockPipeline类，调试接收的item
    
    10、在settings.py 取消 ITEM_PIPELINES 的相关注释，在ITEM_PIPELINES 增加 'stock_spider1.pipelines.StockPipeline': 1,自己的pipeline
    
    11、数据处理在pipelines.py增加StockPipeline类
    '''


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['pycs.greedyai.com/']
    start_urls = ['http://pycs.greedyai.com//']

    def parse(self, response):
        post_urls = response.xpath("//a/@href").extract()
        for post_url in post_urls:
            url = parse.urljoin(response.url, post_url)  #拼接url
            yield  scrapy.Request(url, callback = self.parse_detail, dont_filter=True)  #设置请求url， 设置回掉函数

            pass
        pass

    def parse_detail(self, response):
        #print("回掉函数parse_detail被执行")

        stock_item = StockItem();

        # 董事会成员姓名
        stock_item["names"]  = self.get_tc(response)
        #+性别，
        stock_item["sexes"] = self.get_sex(response)
        # 股票代码
        stock_item["codes"] = self.get_code(response)
        # #年龄
        stock_item["ages"] = self.get_age(response)
        # 职位信息
        stock_item["leaders"] = self.get_leader(response, len(stock_item["names"]))


        #保存到item,并且提交
        yield stock_item

        pass

    def get_tc(self, response):
        tc_names = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()").extract()
        return tc_names
        pass
    def get_sex(self, response):
        #//*[@id=\"ml_001\"]/table/tbody/tr[2]/td[1]/div/table/thead/tr[2]/td[1]
        infos = response.xpath("//*[@class=\"intro\"]/text()").extract()
        sex_list=[]
        for info in infos:
            try:
                sex = re.findall("[男|女]",info)[0]
                sex_list.append(sex)
            except(IndexError):
                continue
        return sex_list
        pass
    def get_age(self, response):
        ages = response.xpath("//*[@class=\"intro\"]/text()").extract()
        age_list = []
        for age in ages:
            try:
                age = re.findall("\d+", age)[0]
                age_list.append(age)
            except(IndexError):  #捕获异常，
                continue
        return age_list
        pass

    def get_code(self, response):  #股票代码
        info_list = response.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/h1/a/@title').extract()
        code_list = []
        for  info in info_list:
            code = re.findall("\d+",info)[0]
            code_list.append(code)
        return code_list
        pass

    def get_leader(self, response, length):
        tc_leaders =  response.xpath("//*[@class=\"tl\"]/text()").extract()
        tc_leaders = tc_leaders[0:length]
        return tc_leaders
        pass

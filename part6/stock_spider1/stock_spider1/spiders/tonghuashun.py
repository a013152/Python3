# -*- coding: utf-8 -*-
import scrapy
#http://stockpage.10jqka.com.cn/600004/company/#detail/

class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'
    allowed_domains = ['stockpage.10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/600004/company.html']


    def parse(self, response):
        #//*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        #//*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        # //*[@id="detail"]/div[2]/div/table/tbody/tr[6]/td[3]/span/div/table/thead/tr[1]/td[1]/h3
        res_selector = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()")  #选择器
        name = res_selector.extract()  #获取选择器的扩展数据
        print(name)

        tc_names = response.xpath("//*[@class=\"tc name\"]/a/text()").extract()
        for tc_name in tc_names:
            print(tc_name)
            pass

        pass


'''
动态页面： 
静态页面：
'''

'''  在 控制台中输入 ：
 scrapy shell http://basic.10jqka.com.cn/600004/company.html
 
 response.xpath("//*[@class=\"tc name\"]/a/text()").extract()  #董事会名单
'''
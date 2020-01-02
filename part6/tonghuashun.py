# -*- coding: utf-8 -*-
import scrapy


class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'
    allowed_domains = ['http://stockpage.10jqka.com.cn/600004/company/#detail']
    start_urls = ['http://http://stockpage.10jqka.com.cn/600004/company/#detail/']

    def parse(self, response):
        pass

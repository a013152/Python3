# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import  re

class StockSpider1Pipeline(object):
    def process_item(self, item, spider):
        return item

class StockPipeline(object):
    def __init__(self):
        self.file = open("D:/excutive_prep.csv","a+")  #追加方式打开文件 D:\excutive_prep.csv，没有则创建

    def process_item(self, item, spider):
        #第一次创建一个文件
        #第一行写标题：高管姓名,性别,年龄,股票代码,职位
        #其余追加到文件末尾
        if os.path.getsize("D:/excutive_prep.csv"):
            # xie
            self.write_content(item)
        else:
            self.file.write("高管姓名,性别,年龄,股票代码,职位\n")

        self.file.flush() #文件写入需要刷新
        return item

    def write_content(self, item):
        names = item["names"]
        sexes = item["sexes"]
        ages = item["ages"]
        codes = item["codes"]
        leaders = item["leaders"]

        result = ""
        for i in range(len(names)):   #拼接字符
            strinfo = re.compile(',')
            str22 = strinfo.sub('+', str(leaders[i]))
            result = names[i]+ "," +sexes[i] + "," +  ages[i]+ "," +codes[i] + "," + str22+ "\n"
            self.file.write(result)
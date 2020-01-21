
'''调式 scrapy'''

from scrapy.cmdline import  execute
import sys
import os
import re

# list=[]
# for i in range(0,10):
#     list.append(str(i)+",")
# str11 = ''.join(list)
# print(str11)
# str11.replace(',' ,'+', 10)
# print(str11)
#
# strinfo = re.compile(',')
# str22 = strinfo.sub('+',str11)
# print(str22)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#execute(["scrapy","crawl","tonghuashun"])
execute(["scrapy","crawl","stock"])

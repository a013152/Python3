'''
安装 pip install scrapy
如果遇到版本问题：
升级版本 python -m pip install --upgrade pip
 pip install --upgrade incremental
依赖： pip install Twisted

'''

import scrapy
html = scrapy.Request("http://stockpage.10jqka.com.cn/600004/company/#detail")
print(html)
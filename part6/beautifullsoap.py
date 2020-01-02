'''
beautifulSoap 是一个从html 或者xml文件中提取数据的python库

pip install beautifulsoup4
'''

from bs4 import BeautifulSoup  #导入beautifulSoup 库
import  re

html_doc="D:/WorkSpace/practice/python/Python3/part6/000004.html"
html_file = open(html_doc,"r", encoding="GBK")
html_handle = html_file.read()   #读取文件

soup =BeautifulSoup(html_handle, 'html.parser')

#print(soup)

#分析heml
#print(soup.head)  #取文档头

#print(soup.p)  #获取p标签

#print(soup.p.attrs)  #获取节点属性

#ps = soup.find_all("p")  #获取所有 p节点
#print(ps)

#result =soup.find_all(id="quotedata")  #获取id 是quotedata 节点信息
#print(result)
#jobs = soup.find_all("strong",class_="the_tit")  #正则筛选
#print(jobs)
#r = re.findall(">(.{2,6})</strong>",str(jobs))
#print(r)

print(soup.title)
print(soup.title.name)  #获取标签名称
print(soup.title.string)  #标签内的文本

# 获取所有的a标签，并遍历打印a标签中的href的值
#for item in soup.find_all("a"):
#    print(item.get("href")) # 获取所有的a标签，并遍历打印a标签的文本值
print(type(soup))

'''正则表达式： 记录文本规则的代码
是一个特殊字符序列
由：字符 + 元字符组成
'''


import re  #导入正则表达式库


#匹配hello字符
# string1 = "123sadfasdfhello123123@!:xiaoqiang"
# reg="hello"
#
# result = re.findall(reg, string1)
# print(result)


'''元字符
. 匹配除了换行符以外的任意字符
\w 匹配字母数字或者划线或者汉字
\s 匹配任意空白符
\d 匹配数字
\b 匹配单词开始或者结束
^  匹配字符串的开始
$  匹配字符串的结束

'''
# reg="\d" #数字
# reg="xiaoqiang$"
# s = re.findall(reg, string1)
# print(s)


'''
限定符
* 重复零次或者多次
+ 重复一次或者多次
？ 重复零次或者一次
{n} 重复n次
{n,} 重复n次或者更多次
'''
#
# reg="\d{5}"
# s=re.findall(reg, string1)
# print(s)

# re.search 只匹配第一个， re.findall匹配所有
# ip_  = "this is ip: 192.168.100.1 : 172.16.0.19"
# reg = "(\d{1,3}.){3}\d{1,3}" #"\d+.\d+.\d+.\d"
# ip_s = re.search(reg, ip_)
# print(ip_s)
#
# #组匹配
#
# phone = "this is phone:13144448888 and this is my postcode:123456"
# reg="this is phone:(\d{11}) and this is my postcode:(\d{6})"
# result = re.search(reg, phone).group(0)
# print(result)


#匹配电话号码
def checkCellphone(cellphone):
    regex="^((13[0-9])|(14[5|7])|(15(0-3]|[5-9]))|(18[0,5-9]))\d{8}$"
    result = re.findall(regex, cellphone )
    if(result):
        print(str(cellphone)+ " 匹配成功")
        return True
    else:
        print(str(cellphone)+ " 匹配失败")
        return False

cellphone= "13144826685"
checkCellphone(cellphone)
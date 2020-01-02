# 声明字符串

s1 = 'hello python'
s2 = "hello python"
s3 = ''' hello 
python
'''

print("s1="+s1+"\ns2="+s2+ "\nS3="+s3);

# 查询
s4 ='Hello python'
print("\ns4[1]="+s4[1])
print("\ns4[0:5]="+s4[0:5])

# 操作
print("s1+s2="+s1+s2)


s1="hello string"
s2="python"
print("s1[:6]+s2="+s1[:6]+s2)

# 包含运算 in
s2='h'
print("s2 in s1="+ str(s2 in s1))
print("s2 not in s1="+ str(s2 not in s1))

# 转义字符 制表符\t 换行符\n 回车符\r \\
print("\'\" \\n")

# 元字符输出
print(R"\t\n\\'\'"+r"\r\n\t\'\*")

# 字符串的格式化输出
print("My name is %s, tody is my %d day study python!"%('LIMEI', 10))

#字符串的内建函数: find, lower, upper replace
findchar ='l';
index1 = s1.find(findchar);
print("s1.find(\"%s\")=%d"%(findchar, index1))

print("s1.lower()=%s\ns1.upper()=%s"%(s1.lower(), s1.upper()))



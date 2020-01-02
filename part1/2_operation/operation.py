'''
基本运算符：  + - * /
# '''
# first_number=12
# second_number=9
# result = first_number+ second_number
# print(result);
#
# first_number=12;
# second_number=9;
# result = first_number-second_number;
# print(result);
#
# first_number = 4
# second_number=5
# result=first_number*second_number;
# print(result)
#
# first_number = 20;
# second_number = 1.9;
# result = first_number/second_number;
# print(result)

'''
算数运算符： %  (取模运算)  **幂运算
'''
i= 10;
j = 3;
print("摸运算i%j="+str(i%j));

z = 3;
print("幂运算j**z="+str(j**z));

z = i//j
print("取整除运算：i//j="+str(z));



'''
进制转换
十进制转二进制
'''

i = 16
j=bin(i);
print("i=16 转二进制="+str(j))
j = oct(i);
print("i=16 转八进制="+str(j))
j=hex(i);
print("i=16 转十六进制="+str(j))
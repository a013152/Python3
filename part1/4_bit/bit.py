i =11
j = 2
z = j&i
print(bin(i))
print(bin(j))
print(z)

z = j|i
print(bin(i))
print(bin(j))
print(z)



'''
按位取反
'''
i=55
z = ~i
print("i="+str(i)+" 二进制为："+bin(i)+ " 按位取反："+str(z)+"二进制为："+str(bin(z)));
# print(z)
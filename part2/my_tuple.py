'''
元组：一个括号内包裹的数据，
 声明后不能修改

'''

l=[1,2,3]
t = (1,2,3)
print("1'type is="+str(type(l))+"\nt'type is="+str(type(t)))
#print(t[3]);

#元组不能修改
t.append(4)
#t
print(t[3])
'''
字典， 可变有序键值容器 ，key：value 组成
不允许同一个键出现两次
'''

d = {"A":1, "B":2, "C":3}
print(d)

keys = d.keys();
values = d.values();
print(str(keys) + str(values))

#add
d["D"] = 4
print(d)

#del
del d["D"]
print(d)

#claer
d.clear();
print(len(d))
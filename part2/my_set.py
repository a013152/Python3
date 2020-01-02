'''
集合：元素不能重复序列
声明方式：{} 或者set()
特性：不重复，无须
'''
def a():
    '''注释注释'''
    pass
print(a.__doc__)

#声明
set_param ={"aaa","bbb","ccc"};
print(set_param)

#判断元素是否在集合内
print("cccc" in set_param)
print("bbb" in set_param)

#集合运算print(str("a | b=") + str(a|b))
a = set('abcdef')
b = set('abcxyz')
'''print(a)
print(b)
print(str("a & b=") + str(a&b))
print(str("a | b=") + str(a|b))
print(str("a ^ b=") + str(a^b))'''

#增加
c = set("abc")
print(c)
c.add("d")
print(c)
#移除
c.remove("b")
print(c)




'''
条件控制
1 比较
==,>, >=, <, <=  只能用在整数
'''

j = "a"
i = "B"
if i < j:
    print("a大")
else:
    print("B大")

print("B  ASCII:"+str(ord(i)))
print("a  ASCII:"+str(ord(j)))

'''
成员运算符合
in ,not in
'''


'''
逻辑运算
and ,or , not

'''
aaaa = [1,2,3,4,5]
if 1 in aaaa and 2 in aaaa and 6 not in aaaa:
    print("1,2,在 aaaa, 6不在aaaa")

def add_bbb(bbb ,add_):
    print("执行add_bbb")
    return bbb + add_;
bbb = 7
if False and add_bbb(bbb, 1) >= 8:
    print("False and ++bbb>8 =>  true : "+ str(bbb))
else:
    print("False and ++bbb>8 =>  false : " + str(bbb))


'''
身份运算符
is 
is not
'''
ccc=7
print(bbb == ccc)
print(ccc is bbb)
print(str(id(ccc)) +"   "+ str(id(bbb)))





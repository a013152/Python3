''' funciotn

函数 定义格式
'''

def my_fun():
    pass


#函数参数
def my_fun_with_param(p1,p2):
    print(p1, p2)

my_fun_with_param(1,2)

# 型参  ，不占用内存地址
#实参， 占用内存
'''
关键字参数 
'''

def my_function_with_params(name, age =10):
    print(name + "l来了，他今年："+ str(age)+"岁")

my_function_with_params(name = "diggg", age =15)  # 关键字参数 name age


'''
函数返回值： 多个值返回的是一个元组
'''
def my_function_with_return(a,b,c):
    return a ,b, c

a =my_function_with_return(1,2,3)
print("a is "+ str(type(a)) + " a len is "+ str(len(a)))

'''
函数返回值： 返回另一个函数
 '''
def return_with_fun(x):
    if 2==x:
        def inner_func(y):
            return y*y
    if 3==x:
        def inner_func(y):
            return y* y* y
    return inner_func

calc = return_with_fun(3);
print(calc(4))



'''递归'''
def recursion(x):
    if 1==x:
        return 1
    return x * recursion(x - 1)
print("递归运算：5 阶乘：" +str(recursion(5)))







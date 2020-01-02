'''变量的作用域


'''
name="bbbbb"
if True:
    name = "hahaha"

def fun():
    def fun2():
        name="cccc"
        print(name)
    fun2()
    print(name)

fun()
print(name)

age = 11
def fun3():
    print(age)
age =12
def fun4():
    age=13
    fun3()
fun4()

def fun5():
    pass
fun5()


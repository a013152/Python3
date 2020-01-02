'''循环

'''

# i =1
# count = 0
# while i<=10:
#     count +=i;
#     i +=1;
#     print("time:"+str(i)+ " count = "+ str(count));
#
# count = 0
# #i = 0
# for i in range(11):
#     count += i;
#     print("time:" + str(i) + " count = " + str(count));



#冒泡
ulist =[1,9,3,2,8,5,6,7,4]

def boddle_sort(l):
    n = len(l) #长度
    for i in range(n -1):
        for j in range(0, n -i -1):
            if l[j+1] < l[j]:
                l[j+1], l[j] = l[j], l[j+1]  # python 两数交换语法， 其他语言 使用temp = l[j+1], l[j+1] = l[j], l[j] = temp
            print("外层i=" + str(i)+",内层j="+str(j)+str(l))

boddle_sort(ulist)
print("排序后")
print(ulist)



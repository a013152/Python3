'''
列表  组数据
list是有序的序列 从0开始

'''

list1 = [111,'222', 333, "444"]
print(type(list1))
print(list1[1:3])

print(list1[2:3])

list1.append(555)
list1.append("6666")
list1 +=[777,"888"]
print(list1)

list2=[[111,'111'],[222,'222']]
len1 = len(list2)
len2 = len(list2[1])
print("len(list2)="+str(len1)+"\nlen(list2[1])="+ str(len2))

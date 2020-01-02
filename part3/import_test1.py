#from part3 import init_test
#相对导入


print("初始化 import_test1")

import part3.second_layer_package.import_test2 as importPack

i =100;
importPack.fun(i)
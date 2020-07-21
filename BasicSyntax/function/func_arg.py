#!/usr/bin/env python
# coding=utf-8

#传递可变类型的参数
def changeme(mylist):
    mylist.append([1, 2, 3, 4]) #在表末尾添加新的对象
    print '函数内的值：', mylist
    return

mylist = [10, 20, 30]
changeme(mylist)
print '函数外的值：', mylist

#传递关键字参数
def printme(str):
    print str
    return

printme(str= 'hds')

#传递不定长参数
def printinfo(arg1, *vartuple): #加了*号的变量名会存放所有未命名的变量参数
    print '输出'
    print arg1
    for var in vartuple:
        print var
    return 

printinfo(10)
printinfo(10, 20, 30)

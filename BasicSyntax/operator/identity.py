#!/usr/bin/env python
# coding=utf-8

#身份运算符
# is: 判断两个标识符是不是引用自一个对象
#     x is y，类似id(x)==id(y)，如果引用的是同一个对象则返回true，否则返回false
# is not: 判断两个标识符是不是引用自不同的对象
#       x is not y，类似id(x)!=id(y)，如果引用的不是同一个对象则返回true，否则返回false
#
# is 与 == 的区别：
#                 is用于判断两个变量引用对象是否为同一个(同一块内存空间)
#                 ==用于判断引用变量的值是否相等
# id()函数用于获取对象的内存地址

a = 20
b = 20
c = 10

if a is b:
    print 'a is b'
else:
    print 'a is not b'

if a is not c:
    print 'a is not c'
else:
    print 'a is c'



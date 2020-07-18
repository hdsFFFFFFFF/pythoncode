#!/usr/bin/env python
# coding=utf-8

#成员运算符
# 成员包括字符串，列表，或元组
# in: 如果x在y序列中，返回true；否则返回false
#not in: 如果x不在y序列中，则返回true；否则返回false

a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list): #不加()括号也可以
    print 'a in list'
else:
    print 'a not in list'

if b not in list:
    print 'b not in list'
else:
    print 'b in list'

a = 3
if a in list:
    print 'a in list'
else:
    print 'a not in list'


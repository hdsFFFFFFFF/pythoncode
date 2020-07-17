#!/usr/bin/env python
# coding=utf-8

#python中的变量赋值不需要类型声明

# 每个变量在使用时必须赋值，变量赋值以后才会被创建
# format：name = value

#python变量赋值不需要类型声明
counter = 100   #整型变量赋值
miles = 1000.0  #浮点型
name = 'John'   #字符串

#多个变量赋值
a = b = c = 1   #将3个变量分配到相同的内存空间上
d, e, f = 1, 100.23, 'hds'


print counter
print miles
print name

print a, b, c   #不换行打印
print d
print e
print f



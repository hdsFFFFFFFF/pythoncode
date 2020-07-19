#!/usr/bin/env python
# coding=utf-8

#通过序列索引迭代
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):    
    #len()返回对象(字符串，列表，元组)长度或条目个数
    #range()函数创建一个整数列表，一般用在for循环中
    print '当前水果', fruits[index]


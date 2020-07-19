#!/usr/bin/env python
# coding=utf-8

#for用来遍历任何序列的条目，如一个列表或一个字符串
#for循环的语法格式：
#       for iterating_var in sequence:
#           statements(s)
#含义:通过for循环依次将<循环序列>中的数据取出赋值给<变量>,再通过<循环体>进行处理
# iterating_var是重复的变量，sequence是序列

for letter in 'python':
    print letter

fruits = ['banana', 'appale', 'mango']
for fruit in fruits:
    print fruit

num_list = [1, 2, 3, 4, 5]
for num in num_list:
    print '当前数字', num

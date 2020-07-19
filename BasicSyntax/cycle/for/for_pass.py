#!/usr/bin/env python
# coding=utf-8

#pass语句一般用于占位置：
#   def func(arg):
#       pass
#   在python2中，如果定义一个空函数程序会报错，当你没有想好
#   函数的内容可以用pass填充，使程序可以正常运行

for letter in 'python':
    if letter == 'h':
        pass
    print '当前字母', letter

#!/usr/bin/env python
# coding=utf-8

#read()方法从一个打开的文件中读取一个字符串
# 语法：fileobject.read(count)
# 在这里，被传递的参数u是要从已打开的文件中读取的字节数。

fd = open('abc.txt', 'r+')
str = fd.read(10)

print str

fd.close()

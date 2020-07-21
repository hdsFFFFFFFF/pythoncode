#!/usr/bin/env python
# coding=utf-8

#write()方法可将任何字符串写入一个打开的文件
# 语法： fileobject.write(string)
# 在这里，被传递的参数是要写入到已打开文件的内容

fo = open('abc.txt', 'w')
fo.write('hello world\n')   #write()方法不会在字符串的结尾添加换行符\n

fo.close()

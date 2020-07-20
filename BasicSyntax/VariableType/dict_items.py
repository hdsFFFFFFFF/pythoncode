#!/usr/bin/env python
# coding=utf-8

#字典items()函数以列表返回可遍历的(键，值)元组数组
# 语法：dict.items()
# items()方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回

dict = {'google':'www.google.com', 'runoob':'www.runoob.com', 'taobao':'www.baobao.com'}

print '字典值:%s' % dict.items()

for key, values in dict.items():
    print key, values

#运行结果
#字典值:
#[('google', 'www.google.com'), ('taobao', 'www.baobao.com'), ('runoob', 'www.runoob.com')]

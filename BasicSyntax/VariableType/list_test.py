#!/usr/bin/env python
# coding=utf-8

#列表的数据项不需要具有相同的类型
# 列表索引从0开始（与字符串的索引一样）
# 列表可以进行截取，组合等
list = ['h', 'd', 's', 'love', 'k', 'c', 'm']
tinylist = [1314]   #list这种写可以，元组这种写不行

print list
print list * 2
print list + tinylist
print tinylist[:]
print list[3]

#使用append()方法来添加列表项
empt_list = []
empt_list.append('google')
empt_list.append('hds')

print empt_list

del empt_list[1]
print empt_list

#!/usr/bin/env python
# coding=utf-8

#字典的每个键值key=>value对用冒号：分割，每个键值对用逗号，分割，整个字典包含在花括号{}中
# d = {key1:value1, key2=value2}
#键key一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一
dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'

tinydict = {'name':'ruboob', 'code':6734, 'dept':'sales'}

print dict['one']   #输出键值为'one'的值
print dict[2]   #输出键值为2的值
print tinydict  #输出完整的字典
print tinydict.keys()   #输出所有键
print tinydict.values() #输出所有值


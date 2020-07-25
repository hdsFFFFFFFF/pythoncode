#!/usr/bin/env python
# coding=utf-8

#split：分裂
#split()函数：通过指定分隔符对字符串进行切片。
# 如果参数num有指定值，则分隔num+1个字符串
str = 'line1-abcd\nline2-abcd\nline3-abcd'
print str.split()   #以空格为分隔符，包含\n

print str.split('a', 1)  #以空格为分隔符，分隔成两个
#运行结果：
#['line1-', 'bcd\nline2-abcd\nline3-abcd']
#以谁为分隔符，就舍去谁。不会再出现在字符串中。
#从第一个遇到的分隔符开始切分
#如果分隔成两个，第一个分隔符会被切掉，后面的不受影响。

str = 'l i n u x'
print str.split()

str = '1 2 3 4 5'
#用a,b,c,d,e分别接收1，2，3，4，5
(a, b, c, d, e) = str.split()

print a, b, c, d, e

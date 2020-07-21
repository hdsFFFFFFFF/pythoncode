#!/usr/bin/env python
# coding=utf-8

fd = open('/proc/meminfo', 'r')

print "name", fd.name
print '是否关闭', fd.closed
print '访问模式', fd.mode

#关闭打开的文件
fd.close()

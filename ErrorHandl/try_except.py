#!/usr/bin/env python
# coding=utf-8

try:
    fd = open('test.txt', 'w')
    fd.write('测试文件\n')
except IOError:
    print 'err:could not find the file or fail to read'
else:
    print 'write success'
    fd.close()

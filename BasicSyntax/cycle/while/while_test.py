#!/usr/bin/env python
# coding=utf-8

count = 0

while count < 9:
    print 'count is ', count
    count += 1

    if count == 8:
        break

    if count % 2 == 0:
        continue
    print '奇数', count
    

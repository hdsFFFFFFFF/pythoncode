#!/usr/bin/env python
# coding=utf-8

#continue用于跳过该次循环
#break用于跳出循环

# 判断条件还可以是一个常值，表示循环必定成立

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print i

i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break
count = 0
while count < 5:
    print count, 'is less than 5'
    count += 1
else:
    print count, 'is not less than 5'

while True:
    num = raw_input('Enter a number:')
    print 'You entered:', num



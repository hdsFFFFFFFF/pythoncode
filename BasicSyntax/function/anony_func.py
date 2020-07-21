#!/usr/bin/env python
# coding=utf-8

#python使用lambda来创建匿名函数
#   lambda只是一个表达式，函数体比def简单很多
#   lambda的主体是一个表达式，而不是一个代码块  \   
#       仅仅能在lambda表达式中封装有限的逻辑进去
#   lambda函数拥有自己的命名空间，且不能访问自有参数列表之外    \
#       或者全局命名空间里的参数
#   虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数  \
#       后者的目的是调用小函数时不用占用栈内存从而增加运行效率
# 
# 语法：lambda [arg1[,arg2, ..., argn]] : expression

sum = lambda arg1, arg2: arg1 + arg2

print '相加后的值为:', sum(10, 10)
print '相加后的值为:', sum(20, 20)

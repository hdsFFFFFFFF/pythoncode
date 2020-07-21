#!/usr/bin/env python
# coding=utf-8

#重命名和删除文件
# os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件
#
# rename():需要两个参数，当前的文件名和新文件名
# os.rename(current_file_name, new_file_name)
#
# remove():删除文件，需要提供要删除的文件名作为参数
# os.remove(file_name)

import os

os.rename('text1.txt', 'text2.txt')
os.remove('text.txt')

# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 10:58
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

info = {'name':'cat', 'age':28}

print(info['name'])
# print(info['job'])
print(info.get('name'))
print(info.get('job'))
print(info.get('job', 'xxx'))
print(info.get('name', 'xxx'))
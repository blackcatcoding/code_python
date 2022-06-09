# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 23:27
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

num = 10

def f1():

    global num
    num += 20
    print("函数1中num =", num)

def f2():

    global num
    num += 30
    print("函数2中num =", num)

f1()
f2()

print(num)
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 11:02
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import turtle as t
import random

t.screensize(800, 600)
t.pencolor('black')
t.speed(7)
t.pensize(5)
t.fillcolor('yellow')

for i in range(5):
    L = random.randint(10, 150)
    x = random.randint(-400 + L, 400 - L)
    y = random.randint(-300 + L, 300 - L)
    t.up()
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    for j in range(5):
        t.fd(L)
        t.right(144)
    t.end_fill()

t.hideturtle()
t.done()
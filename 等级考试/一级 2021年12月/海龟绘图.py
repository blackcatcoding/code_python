# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/13 22:49
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import turtle as t

t.fillcolor('red')
t.speed(1)

# 绘制正方形
for i in range(4):
    t.fd(200)
    t.left(90)


# 绘制菱形
t.pu()
t.goto(100, 0)
t.pd()

t.begin_fill()

t.goto(200, 100)
t.goto(100, 200)
t.goto(0, 100)
t.goto(100, 0)

t.end_fill()

t.hideturtle()
t.done()
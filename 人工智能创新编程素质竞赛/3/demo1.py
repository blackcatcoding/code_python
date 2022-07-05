# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 18:18
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

# 宫保鸡丁,锅包肉,脆皮五花肉,西红柿鸡蛋汤,煲仔饭
foods = {'宫保鸡丁': 25, '锅包肉': 30, '米饭': 3, '汉堡': 15, '可乐': 4,  '脆皮五花肉': 19, '西红柿鸡蛋汤': 10, '烤猪蹄': 25}

books = input('菜单：').split(',')

cnt = 0

for i in books:
    if i in list(foods.keys()):
        print(i, end=' ')
        cnt += foods[i]

print('\n%d' % cnt)

# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 14:51
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

'''
1,3,4,6,7,13,17,21
2,5,6,8,10,12,14,16,18
'''

x = input()
s = x.split(',')
a = []
for i in range(________):
    a.append(int(s[i]))

y = input()
s = y.________
b = []
for i in range(len(s)):
    b.append(int(s[i]))

ret = []
i, j = 0, 0
while len(a) >= i + 1 and ________:
    if a[i] <= b[j]:
        ________
        i += 1
    else:
        ret.append(b[j])
        j += 1

if len(a) > i:
    ret += a[i:]
if len(b) > j:
    ________

print(ret)


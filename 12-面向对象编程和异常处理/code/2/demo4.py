# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 17:09
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

class YangJian:

    def weopon(self):
        print('三尖两刃刀 + 哮天犬')

class WuKong:

    def skill(self):
        print('七十二变 + 筋斗云')

class BlackCat(YangJian, WuKong):

    pass


cat = BlackCat()
cat.weopon()
cat.skill()
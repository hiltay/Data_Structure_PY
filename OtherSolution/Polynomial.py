#!/usr/bin/env python
# -*- coding:utf-8 -*-
import LinkList
# todo 一元多项式抽象数据类型基于链表的操作实现


class Polynomail:
    def __init__(self,):
        self.lenth = 0  # 项数
        self.polynomail = LinkList.LinkList()

    # 输入项数m,创建一元多项式
    def creat_polyn(self, m: int):
        while m:
            coef = input("项数：")
            expn = input("系数：")
            m -= 1

    # 销毁一元多项式
    def destroy_polyn(self):
        pass

    # 打印输出一元多项式
    def print_polyn(self):
        pass

    # 返回一元多项式的项数
    def polyn_lenth(self):
        pass

    # 多项式相加
    def add_polyn(self):
        pass

    # 多项式相减
    def subtract_polyn(self):
        pass

    # 多项式相乘
    def multiply_polyn(self):
        pass

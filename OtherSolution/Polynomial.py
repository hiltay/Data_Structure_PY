#!/usr/bin/env python
# -*- coding:utf-8 -*-


# todo 一元多项式抽象数据类型基于链表的操作实现


class OrderList:

    class __Node:
        def __init__(self, data=None, next=None):
            if data is None:
                data = [None, None]
            self.data = data
            self.next = next

    def __init__(self):
        self.head = self.__Node()

    # 添加元素e
    def order_add(self, e):
        p = self.head
        while p.next:
            if p.next.data[1] < e[1]:
                p = p.next
            else:
                break
        p.next = self.__Node(e, p.next)

    # def print_list(self):
    #     p = self.head
    #     while p:
    #         print(p.data)
    #         p = p.next


class Polynomail:
    def __init__(self):
        self.lenth = 0  # 项数
        self.polyn = OrderList()

    # 成对输入系数和指数[coef,expn],[(3,2),(7,6),(0.3,5)]创建一元多项式
    def creat_polyn(self, param: [[float, int]]):
        for i in param:
            self.polyn.order_add(i)
            self.lenth += 1

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


s = Polynomail()
s.creat_polyn([(3,2),(7,6),(0.3,5)],)


#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 一元多项式抽象数据类型基于链表的操作实现
class Polynomail:
    class __Node:
        def __init__(self, coef=None, expn=None, next=None):
            self.coef = coef  # 系数
            self.expn = expn  # 指数
            self.next = next

    def __init__(self):
        self.head = self.__Node()
        self.__lenth = 0  # 项数

    # 输入系数和指数创建一元多项式
    def create_polyn(self):
        inp = input("输入系数和指数,逗号分隔,任意字母结束>>>").split(",")
        while len(inp) == 2:
            self.__create(self.head, float(inp[0]), int(inp[1]))
            inp = input(">>>").split(",")
        print("你创建的多项式是:")
        self.print_polyn()

    # 有序创建 p:从p结点后创建
    def __create(self, p, coef, expn):
        if self.__lenth == 0:
            self.head.next = self.__Node(coef, expn)
            self.__lenth += 1
            return
        if p.next.expn == expn:
            p.next.coef += coef
            if p.next.coef == 0:
                p.next = p.next.next
                self.__lenth -= 1
            return
        if p.next.expn > expn:
            p = p.next
            if p.next is None:
                p.next = self.__Node(coef, expn)
                self.__lenth += 1
                return
            self.__create(p, coef, expn)
        else:
            p.next = self.__Node(coef, expn, p.next)
            self.__lenth += 1


    # 销毁一元多项式
    def destroy_polyn(self):
        self.__init__()

    # 打印输出一元多项式
    def print_polyn(self):
        ret = []
        p = self.head.next
        while p:
            if p.coef == 0:
                continue
            if p.coef > 0 and ret:
                if p.expn == 0:
                    ret.append("+%.2f" % p.coef)
                    p = p.next
                else:
                    ret.append("+%.2fX^%d" % (p.coef, p.expn))
                    p = p.next
            else:
                if p.expn == 0:
                    ret.append("%.2f" % p.coef)
                    p = p.next
                else:
                    ret.append("%.2fX^%d" % (p.coef, p.expn))
                    p = p.next
        ret = "".join(ret)
        print(ret)

    # 返回一元多项式的项数
    def polyn_lenth(self):
        return self.__lenth

    # 另一个多项式与自己相加
    def add_polyn(self, poly):
        p = poly.head.next
        while p:
            self.__create(self.head, p.coef, p.expn)
            p = p.next
        print("相加后:")
        self.print_polyn()

    # 另一个多项式与自己相减
    def subtract_polyn(self,poly):
        p = poly.head.next
        while p:
            self.__create(self.head, -p.coef, p.expn)
            p = p.next
        print("相减后:")
        self.print_polyn()

    # 多项式相乘
    def multiply_polyn(self, poly):
        p1 = poly.head.next
        tmp = self.head.next
        p2 = tmp
        self.destroy_polyn()
        while p1:
            while p2:
                self.__create(self.head, p1.coef*p2.coef, p1.expn+p2.expn)
                p2 = p2.next
            p2 = tmp
            p1 = p1.next
        print("相乘后:")
        self.print_polyn()

# 测试用例
# if __name__ == '__main__':
#     s1 = Polynomail()
#     s2 = Polynomail()
#     print("创建多项式1")
#     s1.create_polyn()
#     print("创建多项式2")
#     s2.create_polyn()
#     t = s1
#     s1.add_polyn(s2)
#     s1 = t
#     s1.subtract_polyn(s2)
#     s1 = t
#     s1.multiply_polyn(s2)

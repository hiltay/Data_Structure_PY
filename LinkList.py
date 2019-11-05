#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 动态链表
# python采用内部类的方式模拟C、C++的指针创建Node
class LinkList:
    # 节点
    class __Node:
        def __init__(self, e=None, next=None):
            self.elem = e
            self.next = next

    # 构造时创建虚拟头结点
    def __init__(self):
        self.__head = self.__Node()
        self.__size = 0

    # 获取链表中的元素个数
    def get_size(self):
        return self.__size

    # 是否为空
    def is_empty(self):
        return self.__size == 0

    # 从中间添加一个元素
    def insert(self, index, e):
        if index > self.__size or index < 0:
            raise Exception("Index is illegal.")
        # 从虚拟头结点开始
        p = self.__head
        for i in range(index):
            p = p.next
        # newnode = self.__Node(e)
        # newnode.next = p.next
        # p.next = newnode
        # 上面三行等于下面这行
        p.next = self.__Node(e, p.next)
        self.__size += 1

    # 从头添加一个元素
    def add_first(self, e):
        self.insert(0, e)

    # 末尾添加元素
    def add_last(self, e):
        self.insert(self.__size, e)

    # 获取index位置元素
    def get(self, index):
        if index >= self.__size or index < 0:
            raise Exception("Index is illegal.")
        # 从虚拟头结点的下一个位置开始
        p = self.__head.next
        for i in range(index):
            p = p.next
        return p.elem

    # 获取头元素
    def get_first(self):
        return self.get(0)

    # 获取最后一个元素
    def get_last(self):
        return self.get(self.__size - 1)

    # 修改index位置的元素为e
    def set(self, index, e):
        if index >= self.__size or index < 0:
            raise Exception("Index is illegal.")
        p = self.__head.next
        for i in range(index):
            p = p.next
        p.elem = e

    # 是否存在元素e
    def contains(self, e):
        p = self.__head.next
        while p.next:
            if p.elem == e:
                return True
            p = p.next
        return False

    # 移除索引位置的元素
    def remove(self, index):
        if index >= self.__size or index < 0:
            raise Exception("Index is illegal.")
        p = self.__head
        for i in range(index):
            p = p.next
        retnode = p.next
        p.next = retnode.next
        retnode.next = None
        self.__size -= 1
        return retnode.elem

    # 移除第一个元素
    def remove_first(self):
        return self.remove(0)

    # 移除最后一个元素
    def remove_last(self):
        return self.remove(self.__size - 1)


#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 基于链表实现队列
class LinkListQueue:

    # 节点
    class __Node:
        def __init__(self, e=None, next=None):
            self.elem = e
            self.next = next

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # 获取链表中的元素个数
    def get_size(self):
        return self.__size

    # 是否为空
    def is_empty(self):
        return self.__size == 0

    # 添加元素/入队，因为在tail端出队复杂度为O(n)，所以在tail端入队。
    def put(self, e):
        # 当队列只有一个元素时，tail和head在同一位置
        if self.__tail is None:
            self.__tail = self.__Node(e,)
            self.__head = self.__tail
        # tail != head -> 队列不为空
        else:
            self.__tail.next = self.__Node(e,)
            self.__tail = self.__tail.next
        self.__size += 1

    # 取出元素/出队，在head端出队/入队复杂度O(1)
    def get(self):
        if self.is_empty():
            raise Exception("The Queue is empty.")
        ret = self.__head
        self.__head = self.__head.next
        ret.next = None
        self.__size -= 1
        if self.__head is None:
            self.__tail = None
        return ret.elem

    # 查看队首元素
    def get_front(self):
        if self.is_empty():
            raise Exception("The Queue is empty.")
        return self.__head.elem


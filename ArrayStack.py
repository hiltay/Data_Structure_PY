#!/usr/bin/env python
# -*- coding:utf-8 -*-
import Array


# Array实现的Stack也是动态栈,顺序存储
class ArrayStack:
    def __init__(self, capacity=10):
        self.__array = Array.Array(capacity)

    # 获取栈元素个数
    def get_size(self):
        return self.__array.get_size()

    # 栈是否为空
    def is_empty(self):
        return self.__array.is_empty()

    # 添加元素
    def push(self, e):
        self.__array.add_last(e)

    # 取出元素
    def pop(self):
        return self.__array.remove_last()

    # 查看容量
    def get_capacity(self):
        return self.__array.get_capacity()

    # 查看栈顶元素
    def peek(self):
        return self.__array.get_last()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import Array


# 顺序结构的队列，基于数组实现，dequeue复杂度为O(n)
class ArrayQueue:

    # 使用Array创建队列，也是动态队列
    def __init__(self, capacity=10):
        self.__array = Array.Array(capacity)

    # 获取元素个数
    def get_size(self):
        return self.__array.get_size()

    # 是否为空
    def is_empty(self):
        return self.__array.is_empty()

    # 获取容量
    def get_capacity(self):
        return self.__array.get_capacity()

    # 添加元素
    def put(self, e):
        self.__array.add_last(e)

    # 取出元素
    def get(self):
        return self.__array.remove_first()

    # 查看队首元素
    def get_front(self):
        return self.__array.get_first()

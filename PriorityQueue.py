#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MaxHeap


class PriorityQueue:
    def __init__(self):
        self.__maxheap = MaxHeap.MaxHeap()

    # 判断队列是否为空
    def is_empty(self):
        return self.__maxheap.is_empty()

    # 获取队列元素数
    def get_size(self):
        return self.__maxheap.get_size()

    # 入队
    def put(self, e):
        self.__maxheap.add(e)

    # 出队
    def get(self):
        return self.__maxheap.extract_max()

    # 查看队首元素
    def get_front(self):
        return self.__maxheap.findmax()

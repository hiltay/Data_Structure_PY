#!/usr/bin/env python
# -*- coding:utf-8 -*-
import Array


# 最大堆,数组实现
class MaxHeap:
    def __init__(self, capacity=10):
        self.__data = Array.Array(capacity)

    # 返回堆中元素个数
    def get_size(self):
        return self.__data.get_size()

    # 是否为空
    def is_empty(self):
        return self.__data.is_empty()

    # index索引的父节点的索引
    def parent(self, index):
        # 这里索引从0开始
        if index == 0:
            raise Exception("Root node does not have parent node.")
        return (index - 1) // 2

    # index索引的左孩子的索引
    def lchild(self, index):
        return index * 2 + 1

    # index索引的右孩子的索引
    def rchild(self, index):
        return index * 2 + 2

    # 向堆中添加元素e
    def add(self, e):
        self.__data.add_last(e)
        self.__siftup(self.__data.get_size() - 1)

    # 将index位置的元素上浮,使其符合最大堆的性质
    def __siftup(self, index):
        # 递归写法
        if index == 0 or self.__data.get(index) <= self.__data.get(self.parent(index)):
            return
        else:
            self.__data.swap(index, self.parent(index))
            self.__siftup(self.parent(index))

        # 迭代写法
        # while index > 0 and self.__data.get(index) > self.__data.get(self.parent(index)):
        #     self.__data.swap(index, self.parent(index))
        #     index = self.parent(index)

    # 移除并返回堆中最大元素(根结点元素)
    def extract_max(self):
        if self.get_size() < 0:
            raise Exception("Heap underflow.")
        ret = self.__data.get_first()
        self.__data.swap(0, self.__data.get_size() - 1)
        self.__data.remove_last()
        self.__siftdown(0)
        return ret

    # index位置元素下沉,使其符合最大堆的性质,《算导》第三版6.2也叫Heapify
    def __siftdown(self, index):
        # 递归实现
        l = self.lchild(index)
        r = self.rchild(index)
        if l <= self.get_size() - 1 and self.__data.get(l) > self.__data.get(index):
            largest = l
        else:
            largest = index
        if r <= self.get_size() - 1 and self.__data.get(r) > self.__data.get(largest):
            largest = r
        # 如果最大元素是index的某个孩子结点,交换两个结点的值
        if largest != index:
            self.__data.swap(index, largest)
            self.__siftdown(largest)

        # 迭代实现
        # while self.lchild(index) < self.__data.get_size():
        #     left = self.lchild(index)
        #     # 如果index右孩子存在,且比左孩子大,left+=1,此时left是两个孩子中最大的那个
        #     if left + 1 < self.__data.get_size() and self.__data.get(left) < self.__data.get(left+1):
        #         left += 1
        #     # index和最大的孩子比较
        #     if self.__data.get(left) < self.__data.get(index):
        #         return
        #     else:
        #         self.__data.swap(left, index)
        #         index = left

    # 查看堆中最大元素
    def findmax(self):
        return self.__data.get_first()




#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution(object):
    class Array:
        # 构造函数，传入数组容量capacity构造Array；使用python中列表来创建数组
        def __init__(self, capacity=10):
            self.data = list()
            # capacity 表示数组的最大容量
            # self.capacity = capacity
            for i in range(capacity):
                self.data.append(None)
            # size 表示当前数组中的有效元素数
            self.size = 0

        # 获取数组中的元素个数
        def get_size(self):
            return self.size

        # 获取数组的容量
        def get_capacity(self):
            return len(self.data)

        # 数组是否为空
        def is_empty(self):
            return self.size == 0

        # 向数组末尾添加一个元素
        def add_last(self, e):
            self.insert(self.size, e)

        # 向数组开头添加一个元素
        def add_first(self, e):
            self.insert(0, e)

        # 向数组指定位置插入一个元素
        def insert(self, index, e):

            if index < 0 or index > self.size:
                raise Exception("insert failed.Require index >= 0 and index <= size.")
            if self.size == len(self.data):
                self.__resize(2 * len(self.data))
            i = self.size - 1
            while i >= index:
                self.data[i + 1] = self.data[i]
                i -= 1
            self.data[index] = e
            self.size += 1

        # 获取index索引位置的元素
        def get(self, index):
            if index < 0 or index >= self.size:
                raise Exception("Get failed.Index is illegal.")
            return self.data[index]

        # 获取末尾元素
        def get_last(self):
            return self.get(self.size - 1)

        # 获取首元素
        def get_first(self):
            return self.get(0)

        # 修改index索引位置的元素为e
        def set(self, index, e):
            if index < 0 or index >= self.size:
                raise Exception("Set failed.Index is illegal.")
            self.data[index] = e

        # 查找数组中是否有元素e
        def contains(self, e):
            for i in range(self.size):
                if self.data[i] == e:
                    return True
            return False

        # 查找数组中元素e的索引，如果不存在则返回-1
        def find(self, e):
            for i in range(self.size):
                if self.data[i] == e:
                    return i
            return -1

        # 删除index位置的元素，并返回该元素
        def remove(self, index):
            if index < 0 or index >= self.size:
                raise Exception("Remove failed.Index is illegal.")
            ret = self.data[index]
            i = index + 1
            while i < self.size:
                self.data[i - 1] = self.data[i]
                i += 1
            self.size -= 1
            self.data[self.size] = None  # 非必需，可以不写
            # 元素小于数组容量1/4，缩减容量为原来的1/2，避免复杂度震荡
            if self.size == len(self.data) // 4 and len(self.data) // 2 != 0:
                self.__resize(len(self.data) // 2)
            return ret

        # 删除首位置的元素，并返回
        def remove_first(self):
            return self.remove(0)

        # 删除尾位置的元素，并返回
        def remove_last(self):
            return self.remove(self.size - 1)

        # 删除数组中值为e的元素，删除成功返回true，否则为false
        def remove_element(self, e):
            index = self.find(e)
            if index != -1:
                self.remove(index)
                return True
            else:
                return False

        # 修改容量
        def __resize(self, new_capacity):
            new_array = Solution.Array(new_capacity)
            for i in range(self.size):
                new_array.data[i] = self.data[i]
            self.data = new_array.data
    class ArrayStack:
        # 用数组创建栈
        def __init__(self, capacity=10):
            self.__array = Solution.Array(capacity)

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

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Solution.ArrayStack()
        for char in s:
            if char == "{" or char == "(" or char == "[":
                stack.push(char)
            else:
                if stack.is_empty():
                    return False
                if char == ")" and stack.pop() != "(":
                    return False
                if char == "]" and stack.pop() != "[":
                    return False
                if char == "}" and stack.pop() != "{":
                    return False
        if stack.is_empty():
            return True
        else:
            return False

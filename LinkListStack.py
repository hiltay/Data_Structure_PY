#!/usr/bin/env python
# -*- coding:utf-8 -*-
import LinkList


# LinkList实现的栈是动态的，链式存储
class LinkListStack:

    def __init__(self):
        self.__linklist = LinkList.LinkList()

    # 获取栈元素个数
    def get_size(self):
        return self.__linklist.get_size()

    # 栈是否为空
    def is_empty(self):
        return self.__linklist.is_empty()

    # 添加元素
    def push(self, e):
        self.__linklist.add_first(e)

    # 取出元素
    def pop(self):
        return self.__linklist.remove_first()

    # 查看栈顶元素
    def peek(self):
        return self.__linklist.get_first()



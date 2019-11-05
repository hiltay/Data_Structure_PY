#!/usr/bin/env python
# -*- coding:utf-8 -*-
import LinkList


# 链表实现集合
class BSTSet:
    def __init__(self):
        self.linklist = LinkList.LinkList()

    # 元素个数
    def get_size(self):
        return self.linklist.get_size()

    # 是否为空
    def is_empty(self):
        return self.linklist.is_empty()

    # 添加元素,不包含重复元素
    def add(self, e):
        if not self.linklist.contains(e):
            self.linklist.add_first(e)

    # 是否包含元素e
    def search(self, e):
        return self.linklist.contains(e)

    # 删除元素e
    def remove(self, e):
        self.linklist.remove(e)

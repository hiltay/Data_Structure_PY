#!/usr/bin/env python
# -*- coding:utf-8 -*-
import BinarySearchTree


# BST实现集合
class BSTSet:
    def __init__(self):
        self.bst = BinarySearchTree.BST()

    # 元素个数
    def get_size(self):
        return self.bst.get_size()

    # 是否为空
    def is_empty(self):
        return self.bst.is_empty()

    # 添加元素,不包含重复元素
    def add(self, e):
        self.bst.add(e)

    # 是否包含元素e
    def search(self, e):
        return self.bst.search(e)

    # 删除元素e
    def remove(self, e):
        self.bst.remove(e)

#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 二叉搜索树
class BST:
    # 定义节点
    class __Node:
        def __init__(self, e = None, lchild = None, rchild = None):
            self.elem = e
            self.lchild = lchild
            self.rchild = rchild

    def __init__(self):
        self.__root = None
        self.__size = 0

    # 节点数
    def get_size(self):
        return self.__size

    # 是否为空树
    def is_empty(self):
        return self.__size == 0

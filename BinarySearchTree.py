#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 二叉搜索树,不含重复元素
# todo 包含重复元素的二叉搜索树
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

    # 添加元素
    def add(self, e,):
        self.__root = self.__add(self.__root, e)

    # 以node为根添加元素e
    def __add(self, node, e):
        if node is None:
            self.__size += 1
            return self.__Node(e)

        if e < node.elem:
            node.lchild = self.__add(node.lchild, e)
        if e > node.elem:
            node.rchild = self.__add(node.rchild, e)
        return node

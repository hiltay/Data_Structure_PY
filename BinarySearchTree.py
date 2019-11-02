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
    def add(self, e):
        self.__root = self.__add(self.__root, e)

    # 以node为根添加元素e(递归实现)
    def __add(self, node, e):
        if node is None:
            self.__size += 1
            return self.__Node(e)

        if e < node.elem:
            node.lchild = self.__add(node.lchild, e)
        if e > node.elem:
            node.rchild = self.__add(node.rchild, e)
        return node

    # 查询是否包含元素e(递归实现)
    def search(self, e):
        return self.__search(self.__root, e) is not None

    # 以node为根的树是否包含e，包含返回该node，否则返回None
    def __search(self, node, e):
        if node is None or node.elem == e:
            return node
        if e < node.elem:
            return self.__search(node.lchild, e)
        else:
            return self.__search(node.rchild, e)
        # 《算导》里说迭代的效率更高
        # 迭代实现:
        # while node is not None and e != node.elem:
        #     if e < node.elem:
        #         node = node.lchild
        #     else:
        #         node = node.rchild
        # return node

    # 前序遍历
    def preorder(self):
        self.__preorder(self.__root)

    # 以node为根进行前序遍历
    def __preorder(self, node):
        if node:
            print(node.elem)
            self.__preorder(node.lchild)
            self.__preorder(node.rchild)

    # 中序遍历
    def inorder(self):
        self.__inorder(self.__root)

    # 以node为根进行中序遍历
    def __inorder(self, node):
        if node:
            self.__inorder(node.lchild)
            print(node.elem)
            self.__inorder(node.rchild)

    # 后序遍历
    def postorder(self):
        self.__postorder(self.__root)

    # 以node为根进行后序遍历
    def __postorder(self, node):
        if node:
            self.__postorder(node.lchild)
            self.__postorder(node.rchild)
            print(node.elem)

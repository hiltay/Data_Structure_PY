#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 二叉搜索树:映射
class BSTMap:
    # 定义节点
    class __Node:
        def __init__(self, key=None, value=None, lchild=None, rchild=None):
            self.key = key
            self.value = value
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

    # 添加key,value
    def add(self, key, value):
        self.__root = self.__add(self.__root, key, value)

    # 以node为根添加key,value(递归实现)
    def __add(self, node, key, value):
        if node is None:
            self.__size += 1
            return self.__Node(key, value)

        if key < node.key:
            node.lchild = self.__add(node.lchild, key, value)
        elif key > node.key:
            node.rchild = self.__add(node.rchild, key, value)
        else:  # key == node.key,树中已存在该key,修改value
            node.value = value
        return node

    # 返回node为根结点的树中,key所在的结点
    def __getnode(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node
        elif key < node.key:
            return self.__getnode(node.lchild, key)
        else:
            return self.__getnode(node.rchild, key)

    # 是否存在key对应的结点
    def contains(self, key):
        return self.__getnode(self.__root, key) is not None

    # 获取key对应的value,key不存在返回None
    def get(self, key):
        node = self.__getnode(self.__root, key)
        if node:
            return node.value

    # 将key对应的value更新
    def set(self, key, value):
        node = self.__getnode(self.__root, key)
        if node:
            node.value = value
        else:
            raise Exception("Key does not exist!")

    # 寻找node为根的最小元素
    def __minelem(self, node):
        if node.lchild is None:
            return node
        return self.__minelem(node.lchild)

    # 删除node为根的最小元素,返回删除后新树的根
    def __removemin(self, node):
        if node.lchild is None:
            # 保存其右子树
            rightnode = node.rchild
            node.rchild = None
            self.__size -= 1
            return rightnode
        node.lchild = self.__removemin(node.lchild)
        return node

    # 删除key对应结点,并返回value
    def remove(self, key):
        node = self.__getnode(self.__root, key)
        if node:  # node不为空
            self.__root = self.__remove(self.__root, key)
            return node.value

    # 删除以node为根的树中key对应的结点.返回删除后的树的根
    def __remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.lchild = self.__remove(node.lchild, key)
            return node
        if key > node.key:
            node.rchild = self.__remove(node.rchild, key)
            return node
        # 找到待删除结点
        if key == node.key:
            # node左孩子为空,用其右孩子替换node
            if node.lchild is None:
                rightnode = node.rchild
                node.rchild = None
                self.__size -= 1
                return rightnode
            # node右孩子为空,用其左孩子替换node
            if node.rchild is None:
                leftnode = node.lchild
                node.lchild = None
                self.__size -= 1
                return leftnode
            # node既有左孩子,又有右孩子
            if node.lchild and node.rchild:
                # 找到node的后继
                successor = self.__minelem(node.rchild)
                successor.rchild = self.__removemin(node.rchild)
                successor.lchild = node.lchild
                node.lchild = node.rchild = None
                return successor

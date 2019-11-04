#!/usr/bin/env python
# -*- coding:utf-8 -*-
import LinkListStack
import LinkListQueue


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

    # 前序遍历，最常用
    def preorder(self):
        self.__preorder(self.__root)

    # 以node为根进行前序遍历
    def __preorder(self, node):
        if node:
            print(node.elem)
            self.__preorder(node.lchild)
            self.__preorder(node.rchild)

    # 前序遍历非递归实现
    def preorderNR(self):
        # 利用栈记录
        stack = LinkListStack.LinkListStack()
        stack.push(self.__root)
        while not stack.is_empty():
            node = stack.pop()
            print(node.elem)
            if node.rchild:
                stack.push(node.rchild)
            if node.lchild:
                stack.push(node.lchild)

    # 中序遍历, 遍历结果是顺序的
    def inorder(self):
        self.__inorder(self.__root)

    # 以node为根进行中序遍历
    def __inorder(self, node):
        if node:
            self.__inorder(node.lchild)
            print(node.elem)
            self.__inorder(node.rchild)

    # 后序遍历，应用举例：释放内存的过程
    def postorder(self):
        self.__postorder(self.__root)

    # 以node为根进行后序遍历
    def __postorder(self, node):
        if node:
            self.__postorder(node.lchild)
            self.__postorder(node.rchild)
            print(node.elem)

    # 层序遍历
    def levleorder(self):
        # 利用队列
        queue = LinkListQueue.LinkListQueue()
        queue.put(self.__root)
        while not queue.is_empty():
            node = queue.get()
            print(node.elem)
            if node.lchild:
                queue.put(node.lchild)
            if node.rchild:
                queue.put(node.rchild)

    # 寻找最小元素
    def minelem(self):
        if self.__size == 0:
            raise Exception("BST is empty.")
        return self.__minelem(self.__root).elem

    # 寻找node为根的最小元素
    def __minelem(self, node):
        if node.lchild is None:
            return node
        return self.__minelem(node.lchild)

    # 删除最小元素(递归实现)
    def removemin(self):
        r = self.minelem()
        self.__root = self.__removemin(self.__root)
        return r

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

    # 寻找最大元素
    def maxelem(self):
        if self.__size == 0:
            raise Exception("BST is empty.")
        return self.__maxelem(self.__root).elem

    # 寻找node为根的最大元素
    def __maxelem(self, node):
        if node.rchild is None:
            return node
        return self.__maxelem(node.rchild)

    # 删除最大元素(递归实现)
    def removemax(self):
        r = self.maxelem()
        self.__root = self.__removemax(self.__root)
        return r

    # 删除node为根的最大元素,返回删除后新树的根
    def __removemax(self, node):
        if node.rchild is None:
            # 保存其左子树
            leftnode = node.lchild
            node.lchild = None
            self.__size -= 1
            return leftnode
        node.rchild = self.__removemax(node.rchild)
        return node

    # 删除元素e
    def remove(self, e):
        self.__root = self.__remove(self.__root, e)

    # 删除以node为根的树中元素e.返回删除后的树的根
    def __remove(self, node, e):
        if node is None:
            return None
        if e < node.elem:
            node.lchild = self.__remove(node.lchild, e)
            return node
        if e > node.elem:
            node.rchild = self.__remove(node.rchild, e)
            return node
        # 找到待删除元素e
        if e == node.elem:
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
                # 找到node的后继 todo：也可以找node的前驱
                successor = self.__minelem(node.rchild)
                successor.rchild = self.__removemin(node.rchild)
                successor.lchild = node.lchild
                node.lchild = node.rchild = None
                return successor


"""
测试用例
tree = BST()
tree.add(6)
tree.add(3)
tree.add(2)
tree.add(0)
tree.add(5)
tree.add(10)
tree.add(13)
tree.add(20)
tree.add(7)
tree.add(8)
# tree.preorder()
tree.remove(6)
tree.preorder()
"""
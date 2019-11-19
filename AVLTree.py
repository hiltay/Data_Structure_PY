#!/usr/bin/env python
# -*- coding:utf-8 -*-


# AVL树
class AVLTree:
    # 定义节点
    class __Node:
        def __init__(self, key=None, value=None, lchild=None, rchild=None):
            self.key = key
            self.value = value
            self.height = 1  # 高度
            self.lchild = lchild
            self.rchild = rchild

    def __init__(self):
        self.__root = None
        self.__size = 0

    # 返回node结点高度
    def __get_height(self, node):
        if node is None:
            return 0
        return node.height

    # 计算node结点的平衡因子:左子树高度-右子树高度
    def __get_balance_factor(self, node):
        if node is None:
            return 0
        return self.__get_height(node.lchild) - self.__get_height(node.rchild)

    # 节点数
    def get_size(self):
        return self.__size

    # 是否为空树
    def is_empty(self):
        return self.__size == 0

    # 当前树是否是二叉搜索树
    def is_bst(self):
        keys = []  # 存储各个结点的key
        self.__inorder(self.__root, keys)
        for i in range(len(keys) - 1):
            if keys[i] > keys[i + 1]:
                return False
        return True

    # 以node为根进行中序遍历
    def __inorder(self, node, keys):
        if node:
            self.__inorder(node.lchild, keys)
            keys.append(node.key)
            self.__inorder(node.rchild, keys)

    # 当前树是否是平衡二叉树
    def is_balance(self):
        return self.__is_balance(self.__root)

    # node结点为根的树是否是平衡二叉树
    def __is_balance(self, node):
        if node is None:
            return True
        balancefactor = self.__get_balance_factor(node)
        if abs(balancefactor) > 1:
            return False
        return self.__is_balance(node.lchild) and self.__is_balance(node.rchild)

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
        # 更新结点height
        node.height = 1 + max(self.__get_height(node.lchild), self.__get_height(node.rchild))
        # 计算平衡因子
        balancefactor = self.__get_balance_factor(node)

        """维护平衡"""
        # 不平衡发生在向该结点左侧的左侧添加结点时(LL),对该结点右旋
        if balancefactor > 1 and self.__get_balance_factor(node.lchild) >= 0:
            return self.__right_rotate(node)
        # 不平衡发生在向该结点左侧的右侧添加结点时(LR),对该结点的左孩子左旋,再对该节点右旋
        if balancefactor > 1 and self.__get_balance_factor(node.lchild) < 0:
            node.lchild = self.__left_rotate(node.lchild)
            return self.__right_rotate(node)
        # 不平衡发生在向该结点右侧的左侧添加结点时(RL),对该结点的右孩子右旋,再对该节点左旋
        if balancefactor < -1 and self.__get_balance_factor(node.rchild) > 0:
            node.rchild = self.__right_rotate(node.rchild)
            return self.__left_rotate(node)
        # 不平衡发生在向该结点右侧的右侧添加结点时(RR),对该结点左旋
        if balancefactor < -1 and self.__get_balance_factor(node.rchild) <= 0:
            return self.__left_rotate(node)

        return node

    # 右旋,返回新树的根
    #                  y                                        x
    #                /   \                                    /   \
    #              x       T4            右旋               z       y
    #            /   \               ------------>        /  \    /  \
    #           z     T3                                T1    T2 T3  T4
    #         /  \
    #       T1    T2
    def __right_rotate(self, y):
        x = y.lchild
        T3 = x.rchild
        # 向右旋转
        x.rchild = y
        y.lchild = T3
        # 更新height,先y后x
        y.height = 1 + max(self.__get_height(y.lchild), self.__get_height(y.rchild))
        x.height = 1 + max(self.__get_height(x.lchild), self.__get_height(x.rchild))
        return x

    # 左旋,返回新树的根
    #                  y                                        x
    #                /   \                                    /   \
    #              T1     x              左旋               y       z
    #                   /   \        ------------>        /  \    /  \
    #                 T2     z                           T1  T2  T3   T4
    #                       /  \
    #                     T3    T4
    def __left_rotate(self, y):
        x = y.rchild
        T2 = x.lchild
        # 向左旋转
        x.lchild = y
        y.rchild = T2
        # 更新height,先y后x
        y.height = 1 + max(self.__get_height(y.lchild), self.__get_height(y.rchild))
        x.height = 1 + max(self.__get_height(x.lchild), self.__get_height(x.rchild))
        return x

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
        retnode = None
        if key < node.key:
            node.lchild = self.__remove(node.lchild, key)
            retnode = node
        if key > node.key:
            node.rchild = self.__remove(node.rchild, key)
            retnode = node
        # 找到待删除结点
        if key == node.key:
            # node左孩子为空,用其右孩子替换node
            if node.lchild is None:
                rightnode = node.rchild
                node.rchild = None
                self.__size -= 1
                retnode = rightnode
            # node右孩子为空,用其左孩子替换node
            elif node.rchild is None:
                leftnode = node.lchild
                node.lchild = None
                self.__size -= 1
                retnode = leftnode
            # node既有左孩子,又有右孩子
            else:
                # 找到node的后继
                successor = self.__minelem(node.rchild)
                successor.rchild = self.__remove(node.rchild, successor.key)
                successor.lchild = node.lchild
                node.lchild = node.rchild = None
                retnode = successor

        # 对即将返回的结点retnode进行维护
        if retnode is None:
            return None
        # 更新结点height
        retnode.height = 1 + max(self.__get_height(retnode.lchild), self.__get_height(retnode.rchild))
        # 计算平衡因子
        balancefactor = self.__get_balance_factor(retnode)

        """维护平衡"""
        # 不平衡发生在向该结点左侧的左侧添加结点时(LL),对该结点右旋
        if balancefactor > 1 and self.__get_balance_factor(retnode.lchild) >= 0:
            return self.__right_rotate(retnode)
        # 不平衡发生在向该结点左侧的右侧添加结点时(LR),对该结点的左孩子左旋,再对该节点右旋
        if balancefactor > 1 and self.__get_balance_factor(retnode.lchild) < 0:
            retnode.lchild = self.__left_rotate(retnode.lchild)
            return self.__right_rotate(retnode)
        # 不平衡发生在向该结点右侧的左侧添加结点时(RL),对该结点的右孩子右旋,再对该节点左旋
        if balancefactor < -1 and self.__get_balance_factor(retnode.rchild) > 0:
            retnode.rchild = self.__right_rotate(retnode.rchild)
            return self.__left_rotate(retnode)
        # 不平衡发生在向该结点右侧的右侧添加结点时(RR),对该结点左旋
        if balancefactor < -1 and self.__get_balance_factor(retnode.rchild) <= 0:
            return self.__left_rotate(retnode)

        return retnode

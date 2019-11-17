#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 并查集1: quickfind,查询O(1),合并O(n)
class UnionFindSets1:
    def __init__(self, size):
        self.__id = []
        for i in range(size):
            self.__id.append(i)

    # 查看p和q是否所属同一个集合,O(1)
    def isconnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并p和q所属的集合,O(n)
    def union(self, p, q):
        pid = self.__find(p)
        qid = self.__find(q)
        if pid == qid:  # q和q同属一个集合
            return
        for index, elem in enumerate(self.__id):
            if self.__id[index] == pid:
                self.__id[index] = qid

    def get_size(self):
        return len(self.__id)

    # 查找p对应的集合编号,O(1)
    def __find(self, p):
        if 0 > p >= len(self.__id):
            raise Exception("Out of bound.")
        return self.__id[p]


"""
测试用例
u = UnionFindSets1(5)
print(u.get_size(), u.isconnected(1, 2))
u.union(1, 2)
u.union(3, 4)
print(u.get_size(), u.isconnected(1, 4))
"""


# 并查集2: quickunion,查询O(h),合并O(h),h为树的高度
class UnionFindSets2:
    def __init__(self, size):
        self.__parent = []
        for i in range(size):
            self.__parent.append(i)

    def get_size(self):
        return len(self.__parent)

    # 查看p和q是否所属同一个集合,O(h)
    def isconnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并p和q所属的集合,O(h)
    def union(self, p, q):
        p_root = self.__find(p)
        q_root = self.__find(q)
        if p_root == q_root:  # q和q同属一个集合
            return
        self.__parent[p_root] = q_root

    # 查找p对应的集合编号,O(h)
    def __find(self, p):
        if 0 > p >= len(self.__parent):
            raise Exception("Out of bound.")
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p


"""
测试用例
u = UnionFindSets2(5)
print(u.get_size(), u.isconnected(1, 2))
u.union(1, 2)
u.union(2, 4)
print(u.get_size(), u.isconnected(1, 2))
print(u.get_size(), u.isconnected(1, 4))
"""


# 并查集3: 基于并查集2做出优化: union操作让元素个数少的集合指向元素个数多的集合（基于sz的优化）
class UnionFindSets3:
    def __init__(self, size):
        self.__sz = [1] * size  # sz[i]表示以i为根的集合中元素的个数,初始时每个集合指向自己,个数为1
        self.__parent = []
        for i in range(size):
            self.__parent.append(i)

    def get_size(self):
        return len(self.__parent)

    # 查看p和q是否所属同一个集合,O(h)
    def isconnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并p和q所属的集合,O(h)
    def union(self, p, q):
        p_root = self.__find(p)
        q_root = self.__find(q)
        if p_root == q_root:  # q和q同属一个集合
            return
        if self.__sz[p_root] < self.__sz[q_root]:  # 比较p集合的高度和q集合的高度
            self.__parent[p_root] = q_root
            self.__sz[q_root] += self.__sz[p_root]
        else:
            self.__parent[q_root] = p_root
            self.__sz[p_root] += self.__sz[q_root]

    # 查找p对应的集合编号,O(h)
    def __find(self, p):
        if 0 > p >= len(self.__parent):
            raise Exception("Out of bound.")
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p


"""
测试用例
u = UnionFindSets3(5)
print(u.get_size(), u.isconnected(1, 2))
u.union(1, 2)
u.union(2, 4)
print(u.get_size(), u.isconnected(1, 2))
print(u.get_size(), u.isconnected(1, 4))
"""


# 并查集4: 基于并查集3做出优化: union操作让深度低的集合指向深度高的集合（基于rank的优化）
class UnionFindSets4:
    def __init__(self, size):
        self.__rank = [1] * size  # sz[i]表示以i为根的集合中元素的深度,初始时每个集合的深度为1
        self.__parent = []
        for i in range(size):
            self.__parent.append(i)

    def get_size(self):
        return len(self.__parent)

    # 查看p和q是否所属同一个集合,O(h)
    def isconnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并p和q所属的集合,O(h)
    def union(self, p, q):
        p_root = self.__find(p)
        q_root = self.__find(q)
        if p_root == q_root:  # q和q同属一个集合
            return
        if self.__rank[p_root] < self.__rank[q_root]:  # 比较p集合的深度和q集合的深度
            self.__parent[p_root] = q_root  # p根结点指向q根结点
        elif self.__rank[p_root] > self.__rank[q_root]:
            self.__parent[q_root] = p_root  # q根结点指向p根结点
        else:  # p和q深度相等
            self.__parent[q_root] = p_root  # q根结点指向p根结点,p的深度+=1
            self.__rank[p_root] += 1

    # 查找p对应的集合编号,O(h)
    def __find(self, p):
        if 0 > p >= len(self.__parent):
            raise Exception("Out of bound.")
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p


"""
测试用例
u = UnionFindSets4(5)
print(u.get_size(), u.isconnected(1, 2))
u.union(1, 2)
u.union(2, 4)
print(u.get_size(), u.isconnected(1, 2))
print(u.get_size(), u.isconnected(1, 4))
"""


# 并查集5: 基于并查集4做出优化: 在find中进行路径压缩,参考《算导》21章
class UnionFindSets5:
    def __init__(self, size):
        self.__rank = [1] * size  # 添加路径压缩后sz[i]不再表示深度,只表示每个结点的排名
        self.__parent = []
        for i in range(size):
            self.__parent.append(i)

    def get_size(self):
        return len(self.__parent)

    # 查看p和q是否所属同一个集合,O(h)
    def isconnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并p和q所属的集合,O(h)
    def union(self, p, q):
        p_root = self.__find(p)
        q_root = self.__find(q)
        if p_root == q_root:  # q和q同属一个集合
            return
        if self.__rank[p_root] < self.__rank[q_root]:
            self.__parent[p_root] = q_root  # p根结点指向q根结点
        elif self.__rank[p_root] > self.__rank[q_root]:
            self.__parent[q_root] = p_root  # q根结点指向p根结点
        else:
            self.__parent[q_root] = p_root  # q根结点指向p根结点,p的深度+=1
            self.__rank[p_root] += 1

    # 查找p对应的集合编号,O(h)
    def __find(self, p):
        if 0 > p >= len(self.__parent):
            raise Exception("Out of bound.")
        while p != self.__parent[p]:
            self.__parent[p] = self.__parent[self.__parent[p]]  # 当前p结点指向它父结点的父结点,路经压缩后不需要维护rank
            p = self.__parent[p]
        return p


# 并查集6: 基于并查集5做出优化: 使用递归方法进行路径压缩
class UnionFindSets6:
    def __init__(self, size):
        self.__rank = [1] * size  # 添加路径压缩后sz[i]不再表示深度,只表示每个结点的排名
        self.__parent = []
        for i in range(size):
            self.__parent.append(i)

    def get_size(self):
        return len(self.__parent)

    # 查看p和q是否所属同一个集合,O(h)
    def isconnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并p和q所属的集合,O(h)
    def union(self, p, q):
        p_root = self.__find(p)
        q_root = self.__find(q)
        if p_root == q_root:  # q和q同属一个集合
            return
        if self.__rank[p_root] < self.__rank[q_root]:
            self.__parent[p_root] = q_root  # p根结点指向q根结点
        elif self.__rank[p_root] > self.__rank[q_root]:
            self.__parent[q_root] = p_root  # q根结点指向p根结点
        else:
            self.__parent[q_root] = p_root  # q根结点指向p根结点,p的深度+=1
            self.__rank[p_root] += 1

    # 查找p对应的集合编号,O(h)
    def __find(self, p):
        if 0 > p >= len(self.__parent):
            raise Exception("Out of bound.")
        if p != self.__parent[p]:
            self.__parent[p] = self.__find(self.__parent[p])  # p的父结点 指向 p的父结点的根结点
        return self.__parent[p]

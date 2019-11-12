#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 区域和检索 - 数组不可变
class NumArray:
    class IntervalTree:
        def __init__(self, arr, merger):
            if not isinstance(arr, list) or not arr or not merger:
                raise Exception("Can not initialize empty array.")
            self.__data = arr
            self.__tree = [None] * 4 * len(arr)
            self.__merger = merger  # 用户自定义融合器,根据用户需要提供不同的功能
            self.__build_segment_tree(0, 0, len(self.__data) - 1)

        # 容量
        def get_size(self):
            return len(self.__data)

        # 获取index位置元素
        def get(self, index):
            if index < 0 or index >= len(self.__data):
                raise Exception('Index is illegal.')
            return self.__data[index]

        # index索引的左孩子的索引
        def __lchild(self, index):
            return 2 * index + 1

        # index索引的右孩子的索引
        def __rchild(self, index):
            return 2 * index + 2

        # 在tree_index位置的结点创建表示区间[l...r]的线段树
        def __build_segment_tree(self, tree_index, l, r):
            """
            :param tree_index:索引；从哪个结点开始创建
            :param l: 区间左端点
            :param r: 区间右端点
            :return: None
            """
            # 区间长度为1时,l==r
            if l == r:
                self.__tree[tree_index] = self.__data[l]
                return
            # 左右子树结点索引
            left_index = self.__lchild(tree_index)
            right_index = self.__rchild(tree_index)
            # 寻找区间中点mid
            mid = l + (r - l) // 2
            # 先分别创建左右子树
            self.__build_segment_tree(left_index, l, mid)
            self.__build_segment_tree(right_index, mid + 1, r)
            # 根据左右子树创建根结点,根节点融合左右子结点的内容,具体融合方法由用户定义merger
            self.__tree[tree_index] = self.__merger(
                self.__tree[left_index],
                self.__tree[right_index],
            )

        # 查询区间[l...r]的值
        def query(self, query_l, query_r):
            if query_l > query_r or query_l < 0 or query_l >= len(self.__data) \
                    or query_r < 0 or query_r >= len(self.__data):
                raise Exception("Index is illegal")
            return self.__query(0, 0, len(self.__data) - 1, query_l, query_r)

        """
        在以tree_index为根的线段树中的(线段树本身)[l...r]的范围里
        搜索区间(用户指定的)[query_l...query_r]的值
        """

        def __query(self, tree_index, l, r, query_l, query_r):
            """
            :param tree_index: 索引；从哪个结点开始查询
            :param l: 区间左端点
            :param r: 区间右端点
            :param query_l: 需要查询的区间左端点
            :param query_r: 需要查询的区间右端点
            :return: 结点的值
            """
            if l == query_l and r == query_r:  # 要查询的左右端点等于当前的左右端点
                return self.__tree[tree_index]
            # 左右子树结点索引
            left_index = self.__lchild(tree_index)
            right_index = self.__rchild(tree_index)
            # 寻找区间中点mid
            mid = l + (r - l) // 2
            if query_l >= mid + 1:  # 要查询的区间左端点大于区间中点mid,忽略左子树去右子树查询即可
                return self.__query(right_index, mid + 1, r, query_l, query_r)
            if query_r <= mid:  # 要查询的区间右端点小于区间中点mid,忽略右子树去左子树查询即可
                return self.__query(left_index, l, mid, query_l, query_r)
            # 要查询的区间一部分在左子树,一部分在右子树
            result_l = self.__query(left_index, l, mid, query_l, mid)
            result_r = self.__query(right_index, mid + 1, r, mid + 1, query_r)
            return self.__merger(result_l, result_r)

    def __init__(self, nums):
        if len(nums) > 0:
            self.__tree = self.IntervalTree(nums, lambda a, b: a + b)

    def sumRange(self, i: int, j: int) -> int:
        return self.__tree.query(i, j)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

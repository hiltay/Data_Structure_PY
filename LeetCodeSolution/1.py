#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 两数之和
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i,j in enumerate(nums):
            ret = self.contains(nums, target - j, i)
            if ret:
                return [i,ret[0]]
    def contains(self, list, e , exceptidx):
        for i in range(len(list)):
            if list[i] == e and i != exceptidx:
                return [i]
        return False
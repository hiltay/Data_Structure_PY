#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 猜数字
class Solution:
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        ret = 0
        for i,j in enumerate(guess):
            if j == answer[i]:
                ret += 1
        return ret
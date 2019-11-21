#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 387. 字符串中的第一个唯一字符
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26
        for i in range(s.__len__()):
            ind = ord(s[i]) - ord("a")
            freq[ind] += 1
        for i in range(s.__len__()):
            ind = ord(s[i]) - ord("a")
            if freq[ind] == 1:
                return i
        return -1
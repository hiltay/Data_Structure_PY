#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 677. 键值映射
class MapSum:
    class __Node:
        def __init__(self, value = 0):
            self.value = value
            self.next = [None] * 26

    def __init__(self):
        self.__root = self.__Node()

    def insert(self, key: str, val: int) -> None:
        current = self.__root
        for char in key:
            index = ord(char.lower()) - ord('a')
            if current.next[index] is None:
                current.next[index] = self.__Node()
            current = current.next[index]
        current.value = val

    def sum(self, prefix: str) -> int:
        current = self.__root
        for char in prefix:
            index = ord(char.lower()) - ord('a')
            if current.next[index] is None:
                return 0
            current = current.next[index]
        # prefix在Trie中都有相应的结点,遍历它们
        return self.iterate_words(current, 0)

    def iterate_words(self, node, sum):
        if node.value != 0:
            sum += node.value

        for n in node.next:
            if n:
                sum = self.iterate_words(n, sum)
        return sum
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert("aa",3)
# param_2 = obj.sum("a")
# print(param_2)
# obj.insert("ab",2)
# param_2 = obj.sum("a")
# print(param_2)
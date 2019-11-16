#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 添加与搜索单词 - 数据结构设计
class WordDictionary:
    class __Node:
        def __init__(self, isword=False):
            self.isword = isword
            self.next = [None] * 26

    def __init__(self):
        self.__root = self.__Node()

    def addWord(self, word: str) -> None:
        current = self.__root
        for char in word:
            index = ord(char.lower()) - ord('a')
            if current.next[index] is None:
                current.next[index] = self.__Node()
            current = current.next[index]
        if not current.isword:
            current.isword = True

    def search(self, word: str) -> bool:

        return self.__match(self.__root, word, 0)


    def __match(self, node, word, index):
        if index == len(word):
            return node.isword
        char = word[index]
        if char != '.':
            charat = ord(char.lower()) - ord('a')
            if node.next[charat] is None:
                return False
            return self.__match(node.next[charat], word, index + 1)
        else:
            for n in node.next:
                if n and self.__match(n, word, index + 1):
                    return True
            return False

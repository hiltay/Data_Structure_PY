#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 字典树（前缀树）常用来存储、处理字符串
# 用Trie处理英文单词的实现,仅限英文
class Trie:
    class __Node:
        def __init__(self, isword=False):
            self.isword = isword
            self.next = [None] * 26

    def __init__(self):
        self.__root = self.__Node()
        self.__size = 0  # 单词数

    # 单词数量
    def get_size(self):
        return self.__size

    # 添加单词
    def add(self, word: str):
        current = self.__root
        for char in word:
            index = ord(char.lower()) - ord('a')
            if current.next[index] is None:
                current.next[index] = self.__Node()
            current = current.next[index]
        if not current.isword:
            current.isword = True
            self.__size += 1

    # 查询单词是否在Trie中
    def contains(self, word: str):
        current = self.__root
        for char in word:
            index = ord(char.lower()) - ord('a')
            if current.next[index] is None:
                return False
            current = current.next[index]
        # 此时Trie中不一定包含要找的单词，如在panda中查询pan，遍历完'pan'但'n'结点isword == False
        return current.isword  # 根据isword判断

    # 查询是否有单词以prefix为前缀
    def isprefix(self, prefix: str):
        current = self.__root
        for char in prefix:
            index = ord(char.lower()) - ord('a')
            if current.next[index] is None:
                return False
            current = current.next[index]
        # prefix在Trie中都有相应的结点,直接返回True
        return True


"""
测试用例
if __name__ == '__main__':
    trie = Trie()
    words = ['panda', 'pandas', 'apple', 'app', 'banana']
    for word in words:
        trie.add(word)

    print('panda', trie.contains('panda'))
    print('pan', trie.contains('pan'))
    print('pana', trie.isprefix('pana'))
    print('zzz', trie.contains('zzz'))
"""
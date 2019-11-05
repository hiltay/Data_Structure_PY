#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 唯一摩尔斯密码词
class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_dict = {'a': '.-',  'b': '-...',  'c': '-.-.',  'd': '-..',  'e': '.',  'f': '..-.',  'g': '--.',  'h': '....',  'i': '..',  'j': '.---',  'k': '-.-',  'l': '.-..',  'm': '--',  'n': '-.', 'o': '---',  'p': '.--.',  'q': '--.-',  'r': '.-.',  's': '...',  't': '-', 'u': '..-',  'v': '...-',  'w': '.--',  'x': '-..-',  'y': '-.--',  'z': '--..'}
        s = set()
        for i in words:
            code = ""
            for char in i:
                code += morse_dict[char]
            s.add(code)
        return len(s)


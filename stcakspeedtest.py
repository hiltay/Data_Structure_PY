#!/usr/bin/env python
# -*- coding:utf-8 -*-
import LinkListStack
import ArrayStack
import random
import time


def test(s: object, opcount: int) -> float:
    starttime = time.time()
    i = 0
    while i < opcount:
        s.push(random.random())
        i += 1
    i = 0
    while i < opcount:
        s.pop()
        i += 1
    endtime = time.time()
    return endtime - starttime

stk1 = LinkListStack.LinkListStack()
stk2 = ArrayStack.ArrayStack()
t1 = test(stk1, 10000000)
t2 = test(stk2, 10000000)
print(t1, t2,)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 循环队列、数组队列、内置队列的性能测试
import random
import time
import CircularQueue
import ArrayQueue
import queue
import MaxHeap

# def test(q: object, opcount: int) -> float:
#     starttime = time.time()
#     i = 0
#     while i < opcount:
#         q.put(random.random())
#         i += 1
#     i = 0
#     while i < opcount:
#         q.get()
#         i += 1
#     endtime = time.time()
#     return endtime - starttime
#
#
# Q1 = ArrayQueue.ArrayQueue()
# Q2 = CircularQueue.CircularQueue()
# Q3 = queue.Queue()
# t1 = test(Q1, 5000)
# t2 = test(Q2, 5000)
# t3 = test(Q3, 5000)
# print(t1, t2, t3,)


# 最大堆测试
li = []
heap = MaxHeap.MaxHeap()
for i in range(100000):
    heap.add(random.random())

for i in range(100000):
    li.append(heap.extract_max())

for i in range(99999):
    if li[i] < li[i+1]:
        print("错误")
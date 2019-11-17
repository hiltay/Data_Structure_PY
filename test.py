#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time
import CircularQueue
import ArrayQueue
import queue
import Array
import MaxHeap
import PriorityQueue
import UnionFindSets

# 循环队列、数组队列、内置队列、优先队列的性能测试
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
# Q4 = PriorityQueue.PriorityQueue()
# t1 = test(Q1, 5000)
# t2 = test(Q2, 5000)
# t3 = test(Q3, 5000)
# t4 = test(Q4,5000)
# print(t1, t2, t3, t4)


# 最大堆测试
# li = []
# heap = MaxHeap.MaxHeap()
# for i in range(100000):
#     heap.add(random.random())
#
# for i in range(100000):
#     li.append(heap.extract_max())
#
# for i in range(99999):
#     if li[i] < li[i+1]:
#         print("发生错误")


# 6种并查集测试
# def test2(q: object, opcount: int) -> float:
#     starttime = time.time()
#     i = 0
#     while i < opcount:
#         a = random.randint(0, q.get_size()-1)
#         b = random.randint(0, q.get_size()-1)
#         q.union(a,b)
#         i += 1
#     i = 0
#     while i < opcount:
#         a = random.randint(0, q.get_size()-1)
#         b = random.randint(0, q.get_size()-1)
#         q.isconnected(a,b)
#         i += 1
#     endtime = time.time()
#     return endtime - starttime
#
#
# size = 10000
# m = 10000
# u1 = UnionFindSets.UnionFindSets1(size)
# u2 = UnionFindSets.UnionFindSets2(size)
# u3 = UnionFindSets.UnionFindSets3(size)
# u4 = UnionFindSets.UnionFindSets4(size)
# u5 = UnionFindSets.UnionFindSets5(size)
# u6 = UnionFindSets.UnionFindSets6(size)
# t1 = test2(u1, m)
# t2 = test2(u2, m)
# t3 = test2(u3, m)
# t4 = test2(u4, m)
# t5 = test2(u5, m)
# t6 = test2(u6, m)
# print(t1, t2, t3, t4, t5, t6)

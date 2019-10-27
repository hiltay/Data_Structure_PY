#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 设计循环队列
class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = list()
        self.front = 0
        self.rear = 0
        self.size = 0
        for i in range(k + 1):
            self.queue.append(None)

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # 如果队列满，返回False
        if self.isFull():
            return False
        self.queue[self.rear] = value
        # 维护rear和size
        self.rear = (self.rear + 1) % len(self.queue)
        self.size += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        # 如果为空，False
        if self.isEmpty():
            return False
        # 该位置用None补足
        self.queue[self.front] = None
        # 维护front和size
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1
        return True



    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.front == self.rear

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return (self.rear + 1) % len(self.queue) == self.front
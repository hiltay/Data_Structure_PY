#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 基于列表实现，循环队列,dequeue复杂度为O(1)
class CircularQueue:
    # 队首指针front，队尾指针rear
    def __init__(self, capacity=10):
        self.queue = list()
        self.front = 0
        self.rear = 0
        self.size = 0  # todo：不使用size，只使用front和rear
        # 要利用front == rear来判断队列是否为空，所以需要多使用一个不存放元素的空间
        for i in range(capacity + 1):
            self.queue.append(None)

    # 获取容量
    def get_capacity(self):
        return len(self.queue) - 1

    # 判断队列是否为空
    def is_empty(self):
        return self.front == self.rear

    # 判断队列是否满
    def is_full(self):
        return (self.rear + 1) % len(self.queue) == self.front

    # 获取队列元素数
    def get_size(self):
        return self.size

    # 入队
    def put(self, e):
        # 如果队列满，扩容为原来元素的2倍
        if self.is_full():
            self.__resize(self.get_capacity() * 2)
        self.queue[self.rear] = e
        # 维护rear和size
        self.rear = (self.rear + 1) % len(self.queue)
        self.size += 1

    # 修改容量
    def __resize(self, new_capacity):
        new_queue = CircularQueue(new_capacity)
        for i in range(self.size):
            new_queue.queue[i] = self.queue[(self.front + i) % len(self.queue)]
        self.queue = new_queue.queue
        self.front = 0
        self.rear = self.size

    # 出队
    def get(self):
        # 如果为空，异常
        if self.is_empty():
            raise Exception("The queue is empty.")
        ret = self.queue[self.front]
        # 该位置用None补足
        self.queue[self.front] = None
        # 维护front和size
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1
        # 元素个数小于容量1/4，缩容为原来的1/2，但容量不能为0
        if self.size == self.get_capacity() // 4 and self.get_capacity() // 2 != 0:
            self.__resize(self.get_capacity() // 2)
        return ret

    # 查看队首元素
    def get_front(self):
        if self.is_empty():
            raise Exception("The queue is empty.")
        return self.queue[self.front]


# Q = CircularQueue()
# for i in range(10):
#     Q.enqueue(i)
#     print(Q.queue)
#     if i % 3 == 2:
#         Q.dequeue()
#         print(Q.queue)


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 移除链表元素
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def __init__(self):
        self.dummyhead = ListNode(1)

    def removeElements(self, head: ListNode, val: int) -> ListNode:

        self.dummyhead.next = head
        p = self.dummyhead
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return self.dummyhead.next

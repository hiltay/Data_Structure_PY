#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 快速排序
def quicksort(left,right):
    if left > right:
        return
    i = left
    j = right
    s = li[i]
    while i != j:
        # 必须从右开始找
        while li[j] >= s and i < j:
            j -= 1
        while li[i] <= s and i < j:
            i += 1
        if i < j:
            t = li[j]
            li[j] = li[i]
            li[i] = t
    # 基准数归位
    li[left] = li[i]
    li[i] = s
    # 递归处理剩下的
    quicksort(left, i - 1)
    quicksort(i + 1, right)


if __name__ == '__main__':
    li = []
    n = int(input("n个数:"))
    for k in range(n):
        li.append(int(input("第%d个数:" % (k+1))))

    quicksort(0, n-1)
    print(li)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2017. All rights reserved by adminsun.

def bubbleSort(alist):
    for i in xrange(len(alist)):
        print(alist)
        for j in xrange(1,len(alist) - i):
            if alist[j-1] > alist[j]:
                alist[j - 1],alist[j] = alist[j], alist[j - 1]

    return alist

unsorted_list = [6, 7, 8, 9, 2, 3, 1, 4]
print(bubbleSort(unsorted_list))
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2017. All rights reserved by adminsun.

def selectionSort(alist):
    for i in xrange(len(alist)):        
        print(alist)
        min_index = i
        for j in xrange(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]
    return alist

unsorted_list = [6, 7, 8, 9, 2, 3, 1, 4]
print(selectionSort(unsorted_list))
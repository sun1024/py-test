#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2017. All rights reserved by adminsun.

def insertionSort(alist):
    for i, item_i in enumerate(alist):
        print alist
        index = i
        while index > 0 and alist[index - 1] >item_i:
            alist[index] = alist[index - 1]
            index -= 1
        
        alist[index] = item_i

    return alist

unsorted_list = [6, 7, 8, 9, 2, 3, 1, 4]
print(insertionSort(unsorted_list))
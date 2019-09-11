#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:17:04 2019

@author: katezeng
"""
import sys

def merge(s,t):
    merged = []
    if s == []:
        return t
    elif t == []:
        return s
    while s != [] and t != []:
        if s[0] <= t[0]:
            u = s.pop(0)
            merged.append(u)
        else:
            u = t.pop(0)
            merged.append(u)
    if s != []:
        merged += s
    else:
        merged += t
    return merged
    
def mergesort(s):
    output = []
    n = len(s)
    if n == 1:
        return s
    elif n == 2:
        if s[-1] >= s[0]:
            return s
        else:
            # return reversed(s)
            return s[::-1]
    else:
        l = s[0:n//2]
        r = s[n//2:n]
        l = mergesort(l)
        r = mergesort(r)
        output = merge(l, r)
        return output
        
if __name__== '__main__':
    myinput = sys.argv[1].split(',')
    myinput = [float(i) for i in myinput]
    print(mergesort(myinput))
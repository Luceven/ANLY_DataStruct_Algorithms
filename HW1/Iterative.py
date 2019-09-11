#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:24:20 2019

@author: katezeng
"""

import time

#%% iterative
def Fibonacci_Iterative(N):
    A = []
    if N == 0:
        A.append(0)
    if N == 1:
        A.append(0)
        A.append(1)
    else:
        A.append(0)
        A.append(1)
        for i in range(2, N+1):
            A.append(A[i-1] + A[i-2])
    return A[-1]

#%% iterative mod
    
def Fibonacci_Iterative_mod(N):
    A = []
    if N == 0:
        A.append(0)
    if N == 1:
        A.append(0)
        A.append(1)
    else:
        A.append(0)
        A.append(1)
        for i in range(2, N+1):
            A.append((A[i-1] % 65536) + (A[i-2] % 65536))
    return A[-1]

#%% Limit time for running
def limit_time():
    n = 0
    current = 0
    temp = 0
    start = time.time()
    while (time.time() - start) <= 60:
        current = temp
        # comment this for testing mod
        #temp = Fibonacci_Iterative(n)
        # comment this for testing without mod
        temp = Fibonacci_Iterative_mod(n)
        n += 1
    print("The largets N for recursive method is:", n-2, "and result is:", current)
            
#%% main
if __name__== '__main__':
    limit_time()
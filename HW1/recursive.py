#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:49:49 2019

@author: katezeng

recursive methods to compute Fibonacci numbers
"""


import time

#%% Recursive
def Fibonacci_Recursive(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return (Fibonacci_Recursive(N-1)) + (Fibonacci_Recursive(N-2))
        
#%% Recursive after mod
        
def Fibonacci_Recursive_mod(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return (Fibonacci_Recursive_mod(N-1) % 65536) + (Fibonacci_Recursive_mod(N-2) % 65536)
    
#%% Limit time for running
def limit_time():
    n = 0
    current = 0
    temp = 0
    start = time.time()
    while (time.time() - start) <= 60:
        current = temp
        # comment this for testing mod
        #temp = Fibonacci_Recursive(n)
        # comment this for testing without mod
        temp = Fibonacci_Recursive_mod(n)
        n += 1
    print("The largets N for recursive method is:", n-2, "and result is:", current)
            
#%% main
if __name__== '__main__':
    limit_time()
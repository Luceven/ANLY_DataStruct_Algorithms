#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 20:09:11 2019

@author: katezeng
"""

import time

#%% Matrix
## helper function for calculate matrix multiplication
def matrix_mult(Q, T):
    temp = [[Q[0][0] * T[0][0] + Q[0][1] * T[1][0], 
             Q[0][0] * T[0][1] + Q[0][1] * T[1][1]],
            [Q[1][0] * T[0][0] + Q[1][1] * T[1][0],
             Q[1][0] * T[0][1] + Q[1][1] * T[1][1]]]
    
    return temp

def matrix_power(Q, n):
    if n == 1:
        return Q
    elif n == 2:
        return matrix_mult(Q, Q)
    elif n % 2 == 0:
        temp = matrix_power(Q, n/2)
        result = matrix_mult(temp, temp)
    else:
        temp = matrix_power(Q, n // 2)
        add_on = matrix_mult(temp, temp)
        result = matrix_mult(Q, add_on)
    return result
        
        
def Fibonacci_Matrix(N):
    Q = [[0, 1], [1, 1]] # The Fibonacci Q matrix representing F0 F1 F2
    F = [0,1]
    # special case
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        temp = matrix_power(Q, N-1)
        result = temp[1][0] * F[0] + temp[1][1] * F[1]
    return result
    

# testing       
#print(Fibonacci_Matrix(15))
    
#%% Matrix with mod
## helper function for calculate matrix multiplication
def matrix_mult_mod(Q, T):
    temp = [[(Q[0][0] * T[0][0]) % 65536 + (Q[0][1] * T[1][0]) % 65536, 
             (Q[0][0] * T[0][1]) % 65536 + (Q[0][1] * T[1][1]) % 65536],
            [(Q[1][0] * T[0][0]) % 65536 + (Q[1][1] * T[1][0]) % 65536,
             (Q[1][0] * T[0][1]) % 65536 + (Q[1][1] * T[1][1]) % 65536]]
    
    return temp

def matrix_power_mod(Q, n):
    if n == 1:
        return Q
    elif n == 2:
        return matrix_mult_mod(Q, Q)
    elif n % 2 == 0:
        temp = matrix_power_mod(Q, n/2)
        result = matrix_mult_mod(temp, temp)
    else:
        temp = matrix_power_mod(Q, n // 2)
        add_on = matrix_mult_mod(temp, temp)
        result = matrix_mult_mod(Q, add_on)
    return result
        
        
def Fibonacci_Matrix_mod(N):
    Q = [[0, 1], [1, 1]] # The Fibonacci Q matrix representing F0 F1 F2
    F = [0,1]
    # special case
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        temp = matrix_power_mod(Q, N-1)
        result = temp[1][0] * F[0] + temp[1][1] * F[1]
    return result

#%% Limit time for running
def limit_time():
    n = 0
    current = 0
    temp = 0
    start = time.time()
    while (time.time() - start) <= 60:
        current = temp
        # comment this for testing mod
        #temp = Fibonacci_Matrix(n)
        # comment this for testing without mod
        temp = Fibonacci_Matrix_mod(n)
        n += 1
    print("The largets N for recursive method is:", n-2, "and result is:", current)
            
#%% main
if __name__== '__main__':
    limit_time()
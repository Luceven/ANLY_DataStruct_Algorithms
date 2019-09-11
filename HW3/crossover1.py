#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:51:49 2019

@author: katezeng
"""

import random, datetime
from math import ceil, log

######### TEST ##########
test1 = [[1, 7], [2, 4]]
test2 = [[3, 3], [5, 2]]
######### TEST ##########

# addisiont of square matrices (a + b = c)
def matrix_add(A, B):
    n = len(A)
    # C = [[0 for j in range(0, n)] for i in range(0, n)]
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

# subtraction of square matrix (a - b = c)
def matrix_sub(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

# regular matrix multiplication
def matrix_mult(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# the strassen algorithm
def strassen(A, B):
    n = len(A)
    if n <= 4:
        return matrix_mult(A, B)
    else:
        half = n//2
        # top left
        A11 = [[0]*half for _ in range(half)]
        B11 = [[0]*half for _ in range(half)]
        # top right
        A12 = [[0]*half for _ in range(half)]
        B12 = [[0]*half for _ in range(half)]
        # bottom left
        A21 = [[0]*half for _ in range(half)]
        B21 = [[0]*half for _ in range(half)]
        # bottom right
        A22 = [[0]*half for _ in range(half)]
        B22 = [[0]*half for _ in range(half)]
        # middle part for calculation
        temp1 = [[0]*half for _ in range(half)]
        temp2 = [[0]*half for _ in range(half)]
        
        # divide the matrix into 4 sub-matrices
        for i in range(0, half):
            for j in range(0, half):
                A11[i][j] = A[i][j]
                B11[i][j] = B[i][j]
                
                A12[i][j] = A[i][j + half]
                B12[i][j] = B[i][j + half]
                
                A21[i][j] = A[i + half][j]
                B21[i][j] = B[i + half][j]
                
                A22[i][j] = A[i + half][j + half]
                B22[i][j] = B[i + half][j + half]
        
        # strassen calculation from P1 to P7
        temp1 = matrix_add(A11, A22)
        temp2 = matrix_add(B11, B22)
        
        # P1 = (A11 + A22) * (B11 + B22)
        P1 = strassen(temp1, temp2)
        
        # update A21 + A22
        temp1 = matrix_add(A21, A22)
        # P2 = (A21 + A22) * B11
        P2 = strassen(temp1, B11)
        
        # update B12 - B22
        temp2 = matrix_sub(B12, B22)
        # P3 = A11 * (B12 - B22)
        P3 = strassen(A11, temp2)
        
        # update B21 - B11
        temp2 = matrix_sub(B21, B11)
        # P4 = A22 * (B21 - B11)
        P4 = strassen(A22, temp2)
        
        # update A11 + A12
        temp1 = matrix_add(A11, A12)
        # P5 = (A11 + A12) * B22
        P5 = strassen(temp1, B22)
        
        # update A21 - A11
        temp1 = matrix_sub(A21, A11)
        # update B11 + B12
        temp2 = matrix_add(B11, B12)
        # P6 = (A21 - A11) * (B11 + B12)
        P6 = strassen(temp1, temp2)

        # update A12 - A22
        temp1 = matrix_sub(A12, A22)
        # update B21 + B22
        temp2 = matrix_add(B21, B22)
        # P7 = (A12 - A22) * (B21 + B22)
        P7 = strassen(temp1, temp2)
        
        # C11 = P1 + P4 - P5 + P7
        temp1 = matrix_add(P1, P4)
        temp2 = matrix_add(temp1, P7)
        C11 = matrix_sub(temp2, P5)
        
        # C12 = P3 + P5
        C12 = matrix_add(P3, P5)
        
        # C21 = P2 + P4
        C21 = matrix_add(P2, P4)
        
        # C22 = P1 + P3 - P2 + P6
        temp1 = matrix_add(P1, P3)
        temp2 = matrix_add(temp1, P6)
        C22 = matrix_sub(temp2, P2)
        
        # output C
        C = [[0]*n for _ in range(n)]
        for i in range(0, half):
            for j in range(0, half):
                C[i][j] = C11[i][j]
                C[i][j + half] = C12[i][j]
                C[i + half][j] = C21[i][j]
                C[i + half][j + half] = C22[i][j]
        return C
        
# helper function for odd matrix size
def wrapper_strassen(A, B):
    assert type(A) == list and type(B) == list
    assert len(A) == len(A[0]) == len(B) == len(B[0])
    
    nxtpwer2 = lambda n: 2**int(ceil(log(n,2)))
    n = len(A)
    m = nxtpwer2(n)
    # middle part for calculation
    temp1 = [[0]*m for _ in range(m)]
    temp2 = [[0]*m for _ in range(m)]
    for i in range(n):
        for j in range(n):
            temp1[i][j] = A[i][j]
            temp2[i][j] = B[i][j]
    temp3 = strassen(temp1, temp2)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = temp3[i][j]
    return C

# binary matrix generator
def matrix_generator(dim):
    A = [[0]*dim for _ in range(dim)]
    B = [[0]*dim for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            A[i][j] = random.randint(0,1)
            B[i][j] = random.randint(0,1)
    return A, B

# print diag entries of matrix
def print_diag(matrix):
    n = len(matrix)
    res = []
    for i in range(n):
        res.append(matrix[i][i])
    return res

# main function
def main():
    
    """
    dim = 10
    # generate binary matrix for test
    A, B = matrix_generator(dim)
    C1 = wrapper_strassen(A, B)
    C2 = matrix_mult(A, B)
    
    # test strassen
    print(print_diag(C1) == print_diag(C2))
    """
    
    
    for x in range(100, 200, 10):
        ord_start = datetime.datetime.now()
        # generate binary matrix for test
        A, B = matrix_generator(x)
        matrix_mult(A, B)
        ord_stop = datetime.datetime.now()
        print("Dimension", x, " Ordinary matrix mult: ", ord_stop - ord_start)
        
        stras_start = datetime.datetime.now()
        # generate binary matrix for test
        A, B = matrix_generator(x)
        wrapper_strassen(A, B)
        stras_stop = datetime.datetime.now()
        print("Dimension", x, " Strassen algorithm: ", stras_stop - stras_start, "\n")
    
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:22:33 2019

@author: katezeng
"""

import math

def print_neatly(M):
    text = "Buffy the Vampire Slayer fans are sure to get their fix with the DVD release of the show's first season. The three-disc collection includes all 12 episodes as well as many extras. There is a collection of interviews by the show's creator Joss Whedon in which he explains his inspiration for the show as well as comments on the various cast members.  Much of the same material is covered in more depth with Whedon's commentary track for the show's first two episodes that make up the Buffy the Vampire Slayer pilot. The most interesting points of Whedon's commentary come from his explanation of the learning curve he encountered shifting from blockbuster films like Toy Story to a much lower-budget television series. The first disc also includes a short interview with David Boreanaz who plays the role of Angel. Other features include the script for the pilot episodes, a trailer, a large photo gallery of publicity shots and in-depth biographies of Whedon and several of the show's stars, including Sarah Michelle Gellar, Alyson Hannigan and Nicholas Brendon."
    line = text.split(" ")
    n = len(line)

    penalty = [[math.inf]*n for x in range(n)]
    cost = [math.inf]*(n+1)
    cost[0] = 0
    place = [math.inf]*n
    for i in range(0, n):
        for j in range(i, n):
            if M - j + i - sum([len(c) for c in line[i:j+1]]) < 0:
                penalty[i][j] = math.inf
            else:
                if j == n-1 and M - j + i - sum([len(c) for c in line[i:]]) >= 0:
                    penalty[i][j] = 0
                else:
                    penalty[i][j] = (M - j + i - sum([len(c) for c in line[i:j+1]]))**3
    
    for i in range(n):
        for j in range(i + 1):
            if cost[j] + penalty[j][i] < cost[i + 1]:
                cost[i + 1] = penalty[j][i] + cost[j]
                place[i] = j
                
    total = cost[-1]

    lines = []
    
    a = n
    b = 0
    while a >= b:
        lines.append(line[place[a-1]:a])
        a = place[a-1]
        b = place[a-1]
        
    lines = lines[::-1]
    
    print('\n')
    
    for l in lines:
        print(' '.join(word for word in l))

    print("Minimum Penalty with M = ", M, "with cost", total, "\n")  

def main():
    print_neatly(40)
    print_neatly(72)

main()
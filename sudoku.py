# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:01:35 2020

@author: Willem
"""


import numpy as np

grid = [[0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,4,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,8,0,0,0]]
iterations = 0
print(np.matrix(grid))


def check_correct(y,x,n):
    global grid
    
    for p in range(9):
        if grid[y][p] == n:
            return False
        if grid[p][x] == n:
            return False
    x_sq = (x // 3 ) * 3    
    y_sq = (y // 3 ) * 3
    for i in range(3):
        for j in range(3):
            if grid[j+y_sq][i+x_sq] == n:
                return False
    return True


def solve_field():
    global grid
    global iterations
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:                                
                for n in range(1,10):
                    if check_correct(y,x,n):
                        grid[y][x] = n
                        iterations += 1
                        solve_field()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    print(iterations)
                        
solve_field()
            
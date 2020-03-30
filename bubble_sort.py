# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:52:26 2020

@author: Willem
"""


unsorted_list = [3,1,4,2,6,3,7,8,5,2,6,3,5,2,8,4]
iterations = 0

def float_bubble(l):
    end = True
    for i in range(len(l)-1):
        x = l[i]
        y = l[i + 1]
        if x > y:
            l[i] = y
            l[i+1] = x
            print(l)
            end = False
    
    return (l,end)
        

def bubble_sort(l):
    end = False
    global iterations
    while not end:
        l,end = float_bubble(l)
        iterations +=1
    return l

    

print(bubble_sort(unsorted_list))
print(iterations)
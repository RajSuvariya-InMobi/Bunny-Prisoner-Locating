# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:27:26 2017

@author: Deven
"""

def answer(x, y):
    # your code here
    a= 1
    b = x+y-1
    count = 0
    for i in range(1,b+1):
        count +=i
    count -= (b-a)
    count += (x-1)
    return count

if __name__ == '__main__':
    s = answer(5,10)
    print(s)
    
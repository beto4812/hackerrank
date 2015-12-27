#!/bin/python

import sys
import math

splited = raw_input().strip().split(' ')



def fib(fst, scd, n):
    if n==0:
        return fst
    elif n==1:
        return scd
    else:
        return fib(fst,scd,n-1)**2+fib(fst, scd, n-2)

print(fib(int(splited[0]), int(splited[1]), int(splited[2])-1))

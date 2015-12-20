#!/bin/python

import sys
from array import *

def calcCode(n):
    cincos = 0
    tres = 0
    suma = 0
    resi = n
    out = ""
    while True:
        if resi%3==0:
            suma = suma+3
            resi = resi-3
            cincos = cincos+3#just can add 3 5's
        elif resi%5==0 :
            suma = suma+5
            resi = resi-5
            tres = tres+5#just can add 5 3's
        else:
            if resi-5>=0:
                suma = suma+5
                resi = resi-5
                tres = tres+5#just can add 5 3's
            elif resi-3>=0:
                suma = suma+3
                resi = resi-3
                tres = cincos+3#just can add 5 3's
            else: break
        if(suma==n or suma>n):
            break
    for i in range(0, cincos):
        out+="5"
    for i in range(0, tres):
        out+="3"
    if resi == 0: return out
    else: return str("-1")

my_array = array('i',[])

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    my_array.append(n)

for v in my_array:
    #print v
    print calcCode(v)

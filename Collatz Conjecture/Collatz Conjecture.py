# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:34:15 2020

@author: Araib Irshad

"""
#>>>>>>>>>COLLATZ CONJECTURE<<<<<<<<<<<<<<
def collatz(n):
    ls = []
    x = 0
    ls.append(n)
    while x != 1:
       if n%2 == 0:
           x = n/2
           n = x
           ls.append(x)
       else:
           x = 3*n +1
           n = x
           ls.append(x)
    print(ls)
    print('Series end reached in'+' '+str(len(ls)-1)+' '+'steps.')
    return

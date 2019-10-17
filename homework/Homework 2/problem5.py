#!/usr/bin/env python

def fib():
        
    def getFib(n_int):
        if n_int==0 or n_int==1:
            F=n_int
        else:
            F=getFib(n_int-1)+getFib(n_int-2)
        return F
    
    n=input("Please enter a non-negative integer or type stop: ")
 
    if n=='stop':
        return
    elif n.isdigit():
        n_int=int(n)
        print('fib(',n_int,') =',getFib(n_int))
        fib()
    else:
        print("The input argument is not a non-negative integer!")
        fib()
        
    return None
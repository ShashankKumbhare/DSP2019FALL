#!/usr/bin/env python

import time

def fibLoop():
        
    def getFib(n_int):
        if n_int==0 or n_int==1:
            F=n_int
        else:
            F_old=0
            F_curr=1
            for i in range(1,n_int):
                F=F_old+F_curr
                F_old=F_curr
                F_curr=F       
        
        return F
    
    n=input("Please enter a non-negative integer or type stop: ")
 
    if n=='stop':
        return
    elif n.isdigit():
        n_int=int(n)
        print("fib(",n_int,") =",getFib(n_int),"\naverage runtime: ",time.process_time(),"seconds")
        fibLoop()
    else:
        print("The input argument is not a non-negative integer!")
        fibLoop()
        
    return None
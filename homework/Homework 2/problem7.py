#!/usr/bin/env python

def isPrime(n):
    
    def modulus(n,x):
        if (n%x)==0:
            return False       
        else:
            if x<(n/2):
                return modulus(n,x+1)
            else:
                return True
    
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        return modulus(n,2)
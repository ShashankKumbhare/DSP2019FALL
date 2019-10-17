#!/usr/bin/env python

def  getTriangleArea(a):

    area=1/2*abs(a[1][0]*a[2][1]-a[2][0]*a[1][1]-a[0][0]*a[2][1]+a[2][0]*a[0][1]+a[0][0]*a[1][1]-a[1][0]*a[0][1])
        
    return area
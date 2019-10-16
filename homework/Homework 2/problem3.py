#!/usr/bin/env python

from math import pi, exp, sqrt

mu=0
sigma=2
x=1

y=1/sqrt(2*pi)/sigma*exp(-1/2*((x-mu)/sigma)**2)
print(y)
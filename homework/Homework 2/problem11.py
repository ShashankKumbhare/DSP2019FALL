#!/usr/bin/env python

import sys

print("The sum of {} is {}".format( " ".join(sys.argv[1:]), sum(float(e) for e in sys.argv[1:])))



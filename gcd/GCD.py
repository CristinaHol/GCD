#!/usr/bin/python3
import math
import sys

if len(sys.argv)>1:
    gcd = math.gcd(int(sys.argv[1]), int(sys.argv[2]))
    print(gcd)
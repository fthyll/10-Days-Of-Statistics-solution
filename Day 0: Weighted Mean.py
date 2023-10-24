#!/bin/python3

import math
import os
import random
import re
import sys
import math

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    res=[]
    for i in range(0,len(X)):
        res.append(X[i]*W[i])
    print(round(sum(res)/sum(W),1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
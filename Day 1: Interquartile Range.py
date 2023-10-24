#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    S = [v for v,f in zip(values,freqs) for i in range(f)]
    S.sort()
    Q1 = median(S[ : len(S)//2])
    Q3 = median(S[len(S)//2 * -1 :])
    
    print(f"{ Q3-Q1 :.1f}")
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)

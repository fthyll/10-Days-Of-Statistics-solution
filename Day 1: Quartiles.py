#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def median(q):
    if isinstance(q, int):
        return q
    n=len(q)
    if n%2==0:
        return (q[n//2-1]+q[n//2])/2
    else:
        return q[n//2]

def quartiles(arr):
    arr.sort()
    n=len(arr)
    m1=0
    m2=0
    m3=0
    m1=median(arr[0:n//2])
    if n%2==0:
        m3=median(arr[n//2:n])
        m2=median(arr)
    else:
        m3=median(arr[(n//2)+1:n])
        m2=median(arr[n//2])
   
    
    return int(m1),int(m2),int(m3)
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
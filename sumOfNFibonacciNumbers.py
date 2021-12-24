#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sumOfNFibonacciNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def sumOfNFibonacciNumbers(n):
    # Write your code here
    if n==0:
        li=[]
    elif n==1:
        li=[0]
    elif n==2:
        li=[0,1]
    else:
        li=[0,1]
        for n in range(2,n):
            num1=li[-1]
            num2=li[-2]
            li.append(num1+num2)
    return sum(li)
        
        
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumOfNFibonacciNumbers(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re

def sockMerchant(n, ar):
    return sum([ar.count(i)//2 for i in set(ar)])

A = [ 10, 20, 20, 10, 10, 30, 50, 10]
num = 20

sockMerchant(20, A)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
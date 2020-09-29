#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    from_the_begin_sum, from_the_last_sum = 0, 0
    for line_num in range(len(arr)):
        from_the_begin_sum += arr[line_num][line_num]
        from_the_last_sum += arr[line_num][len(arr) - line_num - 1]

    return abs(from_the_begin_sum - from_the_last_sum)
    # Write your code here
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

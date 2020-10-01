#!/bin/python3
## https://www.hackerrank.com/challenges/plus-minus/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    PLUS , MINUS , ZERO = 0, 0, 0
    for i in arr:
        if (i > 0):
            PLUS += 1
        elif ( i < 0 ):
            MINUS += 1
        else:
            ZERO += 1
    print(format((PLUS / len(arr)),".6f"))
    print(format((MINUS / len(arr)),".6f"))
    print(format((ZERO / len(arr)), ".6f"))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

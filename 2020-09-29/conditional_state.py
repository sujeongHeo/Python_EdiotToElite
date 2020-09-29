#!/bin/python3

import math
import os
import random
import re
import sys


# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


if __name__ == '__main__':
    N = int(input())
    if (N % 2 == 1):
        print("Weird")
    elif(N > 2 and N < 6):
        print("Not Weird")
    elif(N > 6 and N < 21):
        print("Weird")
    else:
        print("Not Weird")

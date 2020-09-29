#!/bin/python3
#https://www.hackerrank.com/challenges/30-operators/problem?h_r=email&unlock_token=ab03c25b29310f011d83d172b21509fc23279549&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    num = meal_cost + (meal_cost * 0.01 * tip_percent) + (meal_cost * tax_percent * 0.01)
    num = round(num)
    print(num)
    return num

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

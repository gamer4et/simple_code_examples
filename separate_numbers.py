#!/bin/python3

'''

My solution of https://www.hackerrank.com/challenges/separate-the-numbers

'''



import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def find_next(s,num):
    num += 1
    if len(s)==0:
        return True
    if s[0] == '0':
        return False
    if int(s[:len(str(num))]) == num:
        return find_next(s[len(str(num)):],num)
    if int(s[:len(str(num))+1])==num:
        return find_next(s[len(str(num))+1:],num)
    return False

def separateNumbers(s):
    # Write your code here
    for i in range(1,len(s)//2+1):
        status = find_next(s[i:],int(s[:i]))

        if status:
            print( f"YES {s[:i]}")
            return
    print( "NO")
    return


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)


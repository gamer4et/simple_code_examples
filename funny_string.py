#!/bin/python3

import math
import os
import random
import re
import sys

'''

My solution of https://www.hackerrank.com/challenges/funny-string

'''

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    s_list = [ord(x) for x in s]
    s_reversed = s_list[::-1]
    s_diff = [abs(s_list[i]-s_list[i+1]) for i in range(len(s_list)-1)]
    s_rev_diff = [abs(s_reversed[i]-s_reversed[i+1]) for i in range(len(s_reversed)-1)]
    log =s_diff == s_rev_diff
    if log:
        return "Funny"
    return "Not Funny"

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()


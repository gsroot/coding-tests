#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'starsAndBars' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndex
#  3. INTEGER_ARRAY endIndex
#
from nexon_exam_20210613 import ex_12, ex_12_simple

if __name__ == '__main__':
    with open('input002.txt', 'r') as f:
        s = f.readline()

        startIndex_count = int(f.readline().strip())

        startIndex = []

        for _ in range(startIndex_count):
            startIndex_item = int(f.readline().strip())
            startIndex.append(startIndex_item)

        endIndex_count = int(f.readline().strip())

        endIndex = []

        for _ in range(endIndex_count):
            endIndex_item = int(f.readline().strip())
            endIndex.append(endIndex_item)

        result1 = ex_12.starsAndBars(s, startIndex, endIndex)
        result2 = ex_12_simple.starsAndBars(s, startIndex, endIndex)
        for i in range(len(result1)):
            if result1[i] != result2[i]:
                print(i, result1[i], result2[i], startIndex[i], endIndex[i])

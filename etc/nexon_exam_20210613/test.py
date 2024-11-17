from nexon_exam_20210613 import ex_10, ex_10_simple
import random

import sys
sys.setrecursionlimit(10000000)

if __name__ == '__main__':
    cases = []
    for _ in range(1000000):
        a = random.randint(1, 500)
        b = random.randint(a, 1000)
        cases.append([a, b])
    print(cases)
    print('틀림')
    ex_10.countNumbers(cases)
    print('맞음')
    ex_10_simple.countNumbers(cases)

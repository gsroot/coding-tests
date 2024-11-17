import random
import sys

from nexon_exam_20210613 import ex_12, ex_12_simple

sys.setrecursionlimit(10000000)

if __name__ == '__main__':
    s = ''.join([random.choice(['|', '*']) for _ in range(20)])
    a = [random.randint(1, 10) for _ in range(20)]
    b = [random.randint(10, 20) for _ in range(20)]
    print(s, a, b)
    print('틀림')
    print(ex_12.starsAndBars(s, a, b))
    print('맞음')
    print(ex_12_simple.starsAndBars(s, a, b))

import sys

from collections import Counter

sys.setrecursionlimit(10000000)


def countNumber(start, end, memo, origin_start):
    if start > end:
        return 0
    if start > origin_start:
        return countNumber(origin_start, end, memo, origin_start) - countNumber(
            origin_start, start - 1, memo, origin_start)
    if not memo[end - origin_start]:
        if any(c > 1 for c in Counter(str(end)).values()):
            memo[end - origin_start] = countNumber(start, end - 1, memo, origin_start)
        else:
            memo[end - origin_start] = 1 + countNumber(start, end - 1, memo, origin_start)
    return memo[end - origin_start]


def countNumbers(arr):
    min_n, max_n = 1, 1
    for case in arr:
        min_n, max_n = min(min_n, case[0]), max(max_n, case[1])
    memo = [[] for _ in range(min_n, max_n + 1)]
    for case in arr:
        print(countNumber(case[0], case[1], memo, min_n))


if __name__ == '__main__':
    countNumbers([[17, 35], [8, 74], [6, 46], [24, 25], [17, 44]])
    # 25 75 9 53
    # 25 75 9 29

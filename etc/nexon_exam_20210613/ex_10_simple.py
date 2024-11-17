from collections import Counter


def countNumber(case):
    start, end = case
    qcnt, nqcnt = 0, 0
    if start < 10:
        qcnt = min(end + 1, 10) - start
        start = 10
    for n in range(start, end + 1):
        if any(c > 1 for c in Counter(str(n)).values()):
            nqcnt += 1
        else:
            qcnt += 1
    return qcnt


def countNumbers(arr):
    for case in arr:
        countNumber(case)


if __name__ == '__main__':
    countNumbers([[17, 35], [8, 74], [6, 46], [24, 25], [17, 44]])
    # 25 75 9 53

from collections import defaultdict


def solution(s):
    cnts = defaultdict(int)
    indexes = defaultdict(int)
    for i, c in enumerate(s):
        cnts[c] += 1
        if cnts[c] == 1:
            indexes[c] = i + 1
        elif cnts[c] == 2:
            del indexes[c]
    return min(indexes.values()) if indexes.values() else -1


if __name__ == '__main__':
    print(solution('staticstics'))

def starCnt(s, start, end):
    subs = list(s[start:end + 1])
    for i in [0, -1]:
        while subs and subs[i] == '*':
            subs.pop(i)
    return subs.count('*')


def starsAndBars(s, startIndex, endIndex):
    result = []
    for se_index in zip(startIndex, endIndex):
        result.append(starCnt(s, se_index[0] - 1, se_index[1] - 1))
    return result


if __name__ == '__main__':
    print(starsAndBars('|||**|*|*', [1, 2, 3], [4, 6, 6]))

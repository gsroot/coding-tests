def starCnt(s, start, end, memo):
    subs = list(s[start:end + 1])
    for i in [0, -1]:
        while subs and subs[i] == '*':
            subs.pop(i)
            if i == 0:
                start += 1
            else:
                end -= 1
    if not f"{start}_{end}" in memo:
        memo[f"{start}_{end}"] = subs.count('*')
    return memo[f"{start}_{end}"]


def starsAndBars(s, startIndex, endIndex):
    result = []
    memo = dict()
    for se_index in zip(startIndex, endIndex):
        result.append(starCnt(s, se_index[0] - 1, se_index[1] - 1, memo))
    return result
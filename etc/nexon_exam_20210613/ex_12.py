from bisect import bisect, bisect_left


def starCnt(start, end, bar_indexes):
    if end - start <= 1:
        return 0
    sb_index_index = bisect_left(bar_indexes, start)
    sb_index = bar_indexes[sb_index_index]
    eb_index_index = bisect(bar_indexes, end) - 1
    eb_index = bar_indexes[eb_index_index]
    subs_len = eb_index - sb_index + 1
    if subs_len <= 0:
        return 0
    bar_cnt_in_sub = eb_index_index - sb_index_index + 1
    return subs_len - bar_cnt_in_sub


def starsAndBars(s, startIndex, endIndex):
    result = []
    bar_indexes = [i for i, c in enumerate(s) if c == '|']
    for se_index in zip(startIndex, endIndex):
        result.append(starCnt(se_index[0] - 1, se_index[1] - 1, bar_indexes))
    return result


if __name__ == '__main__':
    print(starsAndBars(
        '|||||******|**|****|******|*|*||*|******|*||**|***|***|**||*|**|***|*|*|**||***|******|*|||*****||||', [5],
        [25]))

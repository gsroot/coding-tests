def getMaxElementIndexes(a, rotate):
    max_index = a.index(max(a))
    result = []
    for r in rotate:
        index = (max_index - (r % len(a))) % len(a)
        result.append(index)
    return result


if __name__ == '__main__':
    print(getMaxElementIndexes([1, 2, 3], list(range(10))))

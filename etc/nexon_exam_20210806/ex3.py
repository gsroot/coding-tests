import random

cache = dict()


def subgrid_sum(grid, i, j, sgsize, maxSum):
    if sgsize == 1:
        if grid[i][j] > maxSum:
            raise Exception()
        return grid[i][j]
    result = 0
    for k in range(sgsize):
        cached = cache.get((i + k, j, j + sgsize + 1))
        if cached:
            row_sum = cached - grid[i + k][j + sgsize + 1]
        else:
            cached = cache.get((i + k, j - 1, j + sgsize))
            if cached:
                row_sum = cached - grid[i + k][j - 1]
        if not cached:
            row_sum = sum(grid[i + k][j:j + sgsize])
        cache[(i + k, j, j + sgsize)] = row_sum
        result += row_sum
        if result > maxSum:
            raise Exception()
    return result


def find_max(grid, n, sgsize, maxSum):
    for i in range(n - sgsize + 1):
        for j in range(n - sgsize + 1):
            subgrid_sum(grid, i, j, sgsize, maxSum)


def largestSubgrid(grid, maxSum):
    n = len(grid)
    total = sum([sum(row) for row in grid])
    if maxSum >= total:
        return n
    result = 0
    for i in reversed(range(n)):
        try:
            find_max(grid, n, i, maxSum)
        except:
            continue
        else:
            return i
    return result


if __name__ == '__main__':
    # with open('input003.txt', 'r') as f:
    #     f.readline()
    #     f.readline()
    #     grid = [[int(y) for y in f.readline().split()] for x in range(100)]
    #     maxSum = int(f.readline())
    grid = [[random.randint(1, 100) for x in range(500)] for y in range(500)]
    maxSum = random.randint(1, 10 ** 6)
    print(largestSubgrid(grid, maxSum))

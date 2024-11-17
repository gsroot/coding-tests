def factorial_recur(n, memo=None):
    if n <= 1:
        return 1
    if memo and n in memo:
        return memo[n]
    val = n * factorial_recur(n - 1, memo)
    if memo:
        memo[n] = val
    return val


def factorial_iter(n, memo=None):
    val = 1
    start = 1
    for i in range(n - 1, 0, -1):
        if memo and i in memo:
            val *= memo[i]
            start = i + 1
            break
        else:
            continue
    for i in range(start, n + 1):
        val *= i
        if memo:
            memo[i] = val
    return val


if __name__ == '__main__':
    memo = {1: 1}
    print(factorial_iter(10000, memo))
    for i in range(10000):
        factorial_iter(9999, memo)
    print('finish')

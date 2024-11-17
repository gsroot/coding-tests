def isPrime(n):
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return i
    else:
        return 1


if __name__ == '__main__':
    print(isPrime(4))

def solution(A):
    move = 0
    A = sorted(A)
    for i in range(len(A)):
        n = i + 1
        if A[i] > n:
            move += A[i] - n
            A[i] -= A[i] - n
        elif A[i] < n:
            move += n - A[i]
            A[i] += n - A[i]
        if move > 1000000000:
            return -1

    return move


if __name__ == '__main__':
    import random

    a = random.randint(1, 10)
    b = [random.randint(1, a) for _ in range(a)]
    print(a, b)
    print(solution(b))

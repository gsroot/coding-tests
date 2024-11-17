def solution(arr, n):
    narr = sorted([x for x in arr if x < n])
    end = len(narr) - 1
    for i in range(end):
        for j in range(end, i, -1):
            if narr[i] + narr[j] == n:
                return True
            if narr[i] + narr[j] < n:
                end = j
                break

    return False


if __name__ == '__main__':
    print(solution([5, 3, 9, 13], 8))
    print(solution([5, 3, 9, 13], 7))
    print(solution([5, 3, 9, 13], 6))
    print(solution([5, 3, 9, 13], 5))
    print(solution([5, 3, 9, 13], 4))
    print(solution([5, 3, 9, 13], 3))
    print(solution([5, 3, 9, 13], 2))
    print(solution([5, 3, 9, 13], 1))

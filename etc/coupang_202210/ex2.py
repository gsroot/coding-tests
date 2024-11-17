def solution(A, S):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return 1 if A[0] >= S else 0
    answer = 0
    current = A[0]
    last_idx = 1
    for i in range(len(A)):
        if current >= S:
            answer = min(answer, j - i + 1) if answer else j - i + 1
            if answer == 1:
                return answer
            current -= A[i]
            continue
        for j in range(last_idx, len(A)):
            if answer and j - i >= answer:
                break
            current += A[j]
            if current >= S:
                answer = min(answer, j - i + 1) if answer else j - i + 1
                last_idx = j + 1
                break
        current -= A[i]
    return answer


if __name__ == '__main__':
    print(solution([1, 10, 2, 9, 4, 8, 3, 7, 5, 6], 20))
    nums = [0, 0]
    print(solution(nums, 10))
    nums = [1, 10]
    print(solution(nums, 10))
    nums = [1, 9, 2]
    print(solution(nums, 10))

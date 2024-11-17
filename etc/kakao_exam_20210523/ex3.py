def solution(arr):
    cases = []
    for n1, n2 in zip(arr, arr[1:]):
        asc = n1 <= n2
        desc = n1 >= n2
        if not cases:
            cases.append([[n1, n2], asc, True])
            continue
        max_len = max([len(x[0]) for x in cases])
        cases = [x for x in cases if x[2] or max_len == len(x[0])]
        prevs = [x for x in cases if x[2]]
        for prev in prevs:
            prev_elms, prev_asc, addable = prev
            if prev_asc:
                prev_elms.append(n2)
                prev[1] = asc
            else:
                if desc:
                    prev_elms.append(n2)
                else:
                    prev[2] = False
        prevs = [x for x in prevs if x[2]]
        if not prevs:
            cases.append([[n1, n2], asc, True])

    return max([len(x[0]) for x in cases]) if cases else 1


if __name__ == '__main__':
    import random

    print(solution([8, 10, 9, 1]))
    print(solution([10, 8, 9, 15, 12, 6, 7]))
    print(solution([5, 1, 2, 1, 4, 5]))
    print(solution([9, 7, 6, 2, 1]))
    print(solution([7, 3, 4, 4, 8, 2, 5, 1]))
    a = random.randint(1, 20)
    b = [random.randint(1, 5) for _ in range(a)]
    print(b)
    print(solution(b))

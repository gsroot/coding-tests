from collections import deque


def bfs(graph, start, visited):
    reorient = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for x in graph[v]:
            if not visited[x if x >= 0 else -x]:
                if x < 0:
                    reorient += 1
                    x = -x
                queue.append(x)
                visited[x] = True
    return reorient


def solution(A, B):
    N = max(max(A), max(B))
    graph = [
        [] for _ in range(N + 1)
    ]
    for i, a in enumerate(A):
        b = B[i]
        graph[b].append(a)
        graph[a].append(-b)

    return bfs(graph, 0, [False for _ in range(N + 1)])


if __name__ == '__main__':
    import random

    A = list(range(100000))
    random.shuffle(A)
    B = list(range(100000))
    random.shuffle(B)
    print(A, B)
    print(solution(A, B))

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
adj = [list(map(int, list(input().rstrip()))) for _ in range(n)]

queue = deque([(0, 0, 0)])

result = 1

prev = dict()

while queue:
    i, cost, path = queue.popleft()
    result = max(result, path.bit_count() + 1)

    if path.bit_count() == n - 1:
        break

    if (i, path) in prev and prev[(i, path)] <= cost:
        continue
    prev[(i, path)] = cost

    for j in range(n):
        if i != j and adj[i][j] >= cost and not path & (1 << j):
            queue.append((j, adj[i][j], path | (1 << i)))

print(result)
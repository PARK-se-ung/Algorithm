import sys
from collections import deque
input = sys.stdin.readline


v, e, k, root = map(int, input().split())
adj = [[] for _ in range(v + 1)]

for _ in range(e):
    start, end = map(int, input().split())
    adj[start].append(end)

queue = deque([(root, 0)])
visited = [False] * (v + 1)
visited[root] = True

result = []

while queue:
    current, depth = queue.popleft()
    if depth == k: 
        result.append(current)
        continue
    for next in adj[current]:
        if not visited[next]:
            visited[next] = True
            queue.append((next, depth + 1))

result.sort()

print(-1 if not result else '\n'.join(map(str, result)))
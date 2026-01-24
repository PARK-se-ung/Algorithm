import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 2):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)
visited[1] = True
queue = deque([1])
first = {1}
while queue:
    current = queue.popleft()
    for next in adj[current]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True
            first.add(next)

second = -1
for i in range(1, n + 1):
    if i not in first:
        second = i
        break

print(f"{1} {second}")
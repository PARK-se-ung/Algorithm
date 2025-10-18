import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    s, e = map(lambda x : int(x) - 1, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [False] * n

component = -1

for i in range(n):
    if not visited[i]:
        queue = deque([i])
        visited[i] = True
        while queue:
            current = queue.popleft()
            for next in adj[current]:
                if not visited[next]:
                    queue.append(next)
                    visited[next] = True
        component += 1

print(component + max(0, m + component - n + 1))
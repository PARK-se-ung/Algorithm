import sys
input = sys.stdin.readline

v = int(input())
adj = [[] for _ in range(v)]
for _ in range(v - 1):
    v1, v2, dist = map(int, input().split())
    adj[v1 - 1].append((v2 - 1, dist))
    adj[v2 - 1].append((v1 - 1, dist))

dist = [-1] * v
dist[0] = 0
result = 0

stack = [0]
while stack:
    current = stack.pop()
    for next, d in adj[current]:
        if dist[next] == -1:
            stack.append(next)
            dist[next] = dist[current] + d

print(max(dist))
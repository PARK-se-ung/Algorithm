import sys
input = sys.stdin.readline
from collections import deque

# well-known; BFS

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

queue = deque([(r1, c1)])
visited = [[-1] * n for _ in range(n)]
visited[r1][c1] = 0

R, C = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

while queue:
    r, c = queue.popleft()
    if r == r2 and c == c2:
        break
    for i in range(6):
        dr, dc = r + R[i], c + C[i]
        if 0 <= dr < n and 0 <= dc < n and visited[dr][dc] == -1:
            visited[dr][dc] = visited[r][c] + 1
            queue.append((dr, dc))

print(visited[r2][c2])
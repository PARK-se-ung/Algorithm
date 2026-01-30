import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
R, C = [-1, 1, 0, 0], [0, 0, -1, 1]

result = 0

for r in range(n):
    for c in range(n):
        if not visited[r][c] and not grid[r][c]:
            component = 1
            queue = deque([(r, c)])
            visited[r][c] = True
            while queue:
                cr, cc = queue.popleft()
                for i in range(4):
                    dr, dc = cr + R[i], cc + C[i]
                    if 0 <= dr < n and 0 <= dc < n:
                        if not visited[dr][dc] and not grid[dr][dc]:
                            queue.append((dr, dc))
                            visited[dr][dc] = True
                            component += 1
            result += (component + k - 1) // k

if result > m or result == 0:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
    print(m - result)
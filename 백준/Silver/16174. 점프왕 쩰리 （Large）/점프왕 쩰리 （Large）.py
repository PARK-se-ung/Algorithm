import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

queue = deque([(0, 0)])
visited[0][0] = True

result = False

while queue:
    r, c = queue.popleft()

    if grid[r][c] == -1:
        result = True
        break

    length = grid[r][c]

    for dr, dc in [(0, length), (length, 0)]:
        newr, newc = r + dr, c + dc
        if 0 <= newr < n and 0 <= newc < n:
            if not visited[newr][newc]:
                queue.append((newr, newc))
                visited[newr][newc] = True


print('HaruHaru' if result else 'Hing')
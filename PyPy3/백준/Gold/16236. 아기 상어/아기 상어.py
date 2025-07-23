import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
grid = []
pos = tuple()
prey = 0
for r in range(n):
    temp = list(map(int, input().split(' ')))
    for c in range(n):
        if temp[c] == 9: pos = (r, c)
        elif temp[c] != 0: prey += 1
    grid.append(temp)

def compare(prev, current):
    if prev[0] > current[0]: return True
    elif prev[0] < current[0]: return False
    elif prev[1] > current[1]: return True
    elif prev[1] < current[1]: return False
    elif prev[2] > current[2]: return True
    return False

time, size, left = 0, 2, 2
R, C = [-1, 0, 0, 1], [0, -1, 1, 0]
def bfs(pos):
    r0, c0 = pos
    queue = deque([(0, r0, c0)])
    visited = [[-1] * n for _ in range(n)]
    grid[r0][c0], visited[r0][c0] = 0, 0
    prev = (float('inf'), -1, -1)
    while queue:
        d, r, c = queue.popleft()
        if d > prev[0]:
            grid[prev[1]][prev[2]] = 9
            return prev[0], (prev[1], prev[2])
        for i in range(4):
            dr, dc = r + R[i], c + C[i]
            if 0 <= dr < n and 0 <= dc < n and visited[dr][dc] == -1:
                if grid[dr][dc] == 0 or grid[dr][dc] == size:
                    visited[dr][dc] = d + 1
                    queue.append((d + 1, dr, dc))
                elif grid[dr][dc] < size:
                    visited[dr][dc] = d + 1
                    if compare(prev, (d + 1, dr, dc)):
                        prev = (d + 1, dr, dc)
                else:
                    visited[dr][dc] = 0
    return prev[0], (prev[1], prev[2])

while True:
    new_time, new_pos = bfs(pos)
    if new_time == float('inf'): break
    else:
        time += new_time
        pos = new_pos
        left -= 1
        if left == 0:
            size += 1
            left = size
print(time)
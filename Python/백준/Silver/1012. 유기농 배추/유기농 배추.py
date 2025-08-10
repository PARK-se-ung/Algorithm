import sys
input = sys.stdin.readline
from collections import deque

R = [-1, 1, 0, 0]
C = [0, 0, -1, 1]

for _ in range(int(input())): # test case
    row, column, num = map(int, input().split(' '))
    # grid
    hibiki = [[0 for _ in range(column)] for _ in range(row)]
    for _ in range(num):
        x, y = map(int, input().split(' '))
        hibiki[x][y] = 1
    # queue
    queue = deque()
    # visited
    visited = [[False for _ in range(column)] for _ in range(row)]
    # answer
    component = 0
    for r in range(row):
        for c in range(column):
            if not queue and not visited[r][c] and hibiki[r][c] == 1: # empty
                queue.append((r, c))
                component += 1
                # BFS
                while queue:
                    r0, c0 = queue.popleft()
                    visited[r0][c0] = True
                    for i in range(4):
                        newr, newc = r0 + R[i], c0 + C[i]
                        if 0 <= newr < row and 0 <= newc < column:
                            if hibiki[newr][newc] == 1 and not visited[newr][newc]:
                                visited[newr][newc] = True
                                queue.append((newr, newc))
    print(component)

import sys
input = sys.stdin.readline
from collections import deque

# BFS로 각 component의 개수를 세기
# 선분으로 막히는 부분은 기록해서 BFS시에 체크

row, column = map(int, input().split())

# 선분으로 막히는 경우 기록
block = set()

for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    if r1 == r2:
        if c1 > c2: c1, c2 = c2, c1
        for c in range(c1, c2):
            block.add((r1 - 1, c, r1, c))
    elif c1 == c2:
        if r1 > r2: r1, r2 = r2, r1
        for r in range(r1, r2):
            block.add((r, c1 - 1, r, c1))

# BFS 세팅
visited = [[False] * column for _ in range(row)]
R, C = [-1, 1, 0, 0], [0, 0, -1, 1]
m, M = row * column, 0

# component 개수 구하기
for r in range(row):
    for c in range(column):
        if not visited[r][c]:
            component = 1
            visited[r][c] = True
            queue = deque([(r, c)])
            while queue:
                r0, c0 = queue.popleft()
                for i in range(4):
                    dr, dc = r0 + R[i], c0 + C[i]
                    if 0 <= dr < row and 0 <= dc < column and not visited[dr][dc]:
                        if (r0, c0, dr, dc) not in block and (dr, dc, r0, c0) not in block:
                            visited[dr][dc] = True
                            queue.append((dr, dc))
                            component += 1
        m, M = min(m, component), max(M, component)

print(f"{M}\n{m}")
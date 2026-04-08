import sys
input = sys.stdin.readline

row, column = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(row)]
rest = []
for r in range(row):
    for c in range(column):
        rest.append((grid[r][c], r, c))
rest.sort(key = lambda x : x[0])

visited = [[False] * column for _ in range(row)]
R, C = [0, 0, -1, -1, -1, 1, 1, 1], [-1, 1, -1, 0, 1, -1, 0, 1]
result = 0

while rest:
    value, r, c = rest.pop()
    if visited[r][c]: continue

    stack = [(value, r, c)]
    visited[r][c] = True
    while stack:
        v, r, c = stack.pop()
        for i in range(8):
            dr, dc = r + R[i], c + C[i]
            if 0 <= dr < row and 0 <= dc < column:
                if not visited[dr][dc] and grid[dr][dc] <= v:
                    visited[dr][dc] = True
                    stack.append((grid[dr][dc], dr, dc))
    result += 1

print(result)
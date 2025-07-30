import sys
input = sys.stdin.readline

row, column, k = map(int, input().split(' '))
grid = list(list(input().rstrip()) for _ in range(row))


R, C = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(pos, distance, visited):
    if distance == k:
        if pos == (0, column - 1):
            return 1
        else:
            return 0
    result = 0
    r, c = pos
    visited[r][c] = True
    for i in range(4):
        dr, dc = r + R[i], c + C[i]
        if 0 <= dr < row and 0 <= dc < column:
            if not visited[dr][dc] and grid[dr][dc] != 'T':
                visited[dr][dc] = True
                result += dfs((dr, dc), distance + 1, visited)
                visited[dr][dc] = False
    return result

visited = [[False] * column for _ in range(row)]
start = (row - 1, 0)
print(dfs(start, 1, visited))

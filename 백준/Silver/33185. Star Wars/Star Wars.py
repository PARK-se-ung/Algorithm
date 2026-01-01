import sys
input = sys.stdin.readline
row, column = map(int, input().split())

grid = [list(input().rstrip()) for _ in range(row)]
dp = [[0] * column for _ in range(row)]
visited = [[False] * column for _ in range(row)]

for r in range(row - 1, 0, -1):
    for c in range(column):
        if grid[r][c] == 'W' or visited[r][c]:
            for i in range(-1, 2):
                dc = c + i
                if 0 <= dc < column:
                    visited[r - 1][dc] = True
                    if grid[r - 1][dc] == 'B':
                        dp[r - 1][dc] = max(dp[r - 1][dc], dp[r][c] + 1)
                    elif grid[r - 1][dc] == '.':
                        dp[r - 1][dc] = max(dp[r - 1][dc], dp[r][c])

print(max(max(dp[i]) for i in range(row)))
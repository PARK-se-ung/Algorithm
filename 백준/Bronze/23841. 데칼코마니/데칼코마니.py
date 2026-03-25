import sys
input = sys.stdin.readline

row, column = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(row)]

for r in range(row):
    for c in range(column):
        if grid[r][c] != '.':
            grid[r][column - 1 - c] = grid[r][c]
        elif grid[r][column - 1 - c] != '.':
            grid[r][c] = grid[r][column - 1 - c]

print('\n'.join(''.join(grid[r]) for r in range(row)))
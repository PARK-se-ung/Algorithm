import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    row, column = [0] * n, [0] * n
    for r in range(n):
        for c in range(n):
            row[r] += grid[r][c]
            column[c] += grid[r][c]
    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())
        r_bias, c_bias = v * (c2 - c1 + 1), v * (r2 - r1 + 1)
        for r in range(r1 - 1, r2):
            row[r] += r_bias
        for c in range(c1 - 1, c2):
            column[c] += c_bias
    print(*row)
    print(*column)
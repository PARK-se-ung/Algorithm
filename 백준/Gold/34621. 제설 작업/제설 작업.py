import sys
input = sys.stdin.readline

row, column = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(row)]

prefix_row = [0] * row
prefix_column = [0] * column

for r in range(row):
    for c in range(column):
        prefix_row[r] += grid[r][c]
        prefix_column[c] += grid[r][c]

def func(arr):
    min_value, idx = float('inf'), -1
    for i in range(len(arr)):
        if arr[i] < min_value:
            min_value, idx = arr[i], i

    return (min_value, idx)

result = -1

for _ in range(row + column):
    min_r, idx_r = func(prefix_row)
    min_c, idx_c = func(prefix_column)
    result = max(result, min(min_r, min_c))

    if min_r <= min_c:
        prefix_row[idx_r] = float('inf')
        for t in range(column):
            prefix_column[t] -= grid[idx_r][t]
    else:
        prefix_column[idx_c] = float('inf')
        for t in range(row):
            prefix_row[t] -= grid[t][idx_c]

print(result)
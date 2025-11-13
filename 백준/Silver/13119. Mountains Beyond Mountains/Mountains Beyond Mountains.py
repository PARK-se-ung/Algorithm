import sys
input = sys.stdin.readline

row, column, h = map(int, input().split())
m = list(map(int, input().split()))

result = [['.'] * column for _ in range(row)]

for c in range(column):
    for r in range(min(row - m[c], row - h), row):
        if r < row - h:
            result[r][c] = '#'
        elif r == row - h:
            if m[c] >= h:
                result[r][c] = '*'
            else:
                result[r][c] = '-'
        else:
            if r >= row - m[c]:
                result[r][c] = '#'
            elif c % 3 == 2:
                result[r][c] = '|'
for i in range(row):
    print(''.join(result[i]))
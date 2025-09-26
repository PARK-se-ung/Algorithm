import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    for j in range(c - 1):
        picture[i][j + 1] += picture[i][j]
for i in range(r - 1):
    for j in range(c):
        picture[i + 1][j] += picture[i][j]

def size(r1, c1, r2, c2, picture):
    result = picture[r2][c2]
    if r1 > 0: result -= picture[r1 - 1][c2]
    if c1 > 0: result -= picture[r2][c1 - 1]
    if r1 > 0 and c1 > 0: result += picture[r1 - 1][c1 - 1]
    return result 

for _ in range(q):
    r1, c1, r2, c2 = map(lambda x : int(x) - 1, input().split())
    n = (r2 - r1 + 1) * (c2 - c1 + 1)
    print(size(r1, c1, r2, c2, picture) // n)
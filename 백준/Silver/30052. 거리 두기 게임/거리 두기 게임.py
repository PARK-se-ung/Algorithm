import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = n + m - 2 - int(input())
block = [[True] * m for _ in range(n)]
for i in range(2):
    for j in range(2):
        block[-i][-j] = False

blank = [(0, 0), (n - 1, 0), (0, m - 1), (n - 1, m - 1)]
R, C = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(k):
    new_blank = []
    while blank:
        r, c = blank.pop()
        for i in range(4):
            dr, dc = r + R[i], c + C[i]
            if 0 <= dr < n and 0 <= dc < m:
                if block[dr][dc]:
                    block[dr][dc] = False
                    new_blank.append((dr, dc))
    blank = new_blank

print(sum(sum(1 for j in range(m) if block[i][j]) for i in range(n)))
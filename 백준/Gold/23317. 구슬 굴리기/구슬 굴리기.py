import sys
input = sys.stdin.readline


n, m = int(input()), int(input())

dp = [[1] * (i + 1) for i in range(n)]

for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

result = 1
r0, c0 = 0, 0

place = [tuple(map(int, input().split(' '))) for _ in range(m)]
place.sort(key = lambda x : x[0])

for i in range(m):
    r, c = place[i]
    if 0 <= c - c0 <= r - r0:
        result *= dp[r - r0][c - c0]
    else:
        result = 0
        break
    r0, c0 = r, c

print(result * sum(dp[n - 1 - r0]))
import sys
input = sys.stdin.readline

# input
n, m = map(int, input().split())
S = list(map(int, input().split()))
a, d = map(int, input().split())

# dp
k = n // d + 1
dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(k):
    for j in range(d * i, n):
        dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + S[j])
        dp[i + 1][min(j + d, n)] = max(dp[i + 1][min(j + d, n)], dp[i][j] + a)


# output
result = -1
for j in range(k + 1):
    if dp[j][n] >= m:
        result = j
        break

print(result)
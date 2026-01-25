import sys
input = sys.stdin.readline

d, m = map(int, input().split())
dp = [[0] * (d // 2 + 1 - abs(i)) for i in range(-d // 2, d // 2)]
dp[0][0] = dp[1][1] = 1

for i in range(1, d):
    if i < d // 2:
        dp[i + 1][2] = dp[i][1]
        for j in range(2, i + 1):
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % m
            dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % m
    elif i > d // 2:
        for j in range(1, d + 1 - i):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % m

print(dp[d - 1][1])
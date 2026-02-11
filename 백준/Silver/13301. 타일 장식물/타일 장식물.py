import sys
input = sys.stdin.readline

n = int(input())
pibo = [1] * (n + 1)
dp = [4] * n
for i in range(1, n):
    pibo[i + 1] = pibo[i] + pibo[i - 1]
    dp[i] = dp[i - 1] + 2 * pibo[i]

print(dp[-1])
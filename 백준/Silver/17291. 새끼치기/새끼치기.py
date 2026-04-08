import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, 0] for _ in range(4)]
dp[0][1] = 1

for i in range(n - 1):
    cnt = 0
    for j in range(3, -1, -1):
        for k in range(2):
            cnt += dp[j][k]
            if j > 0: dp[j][k] = dp[j - 1][k]
    dp[0], dp[3][1] = [0, 0], 0
    dp[0][i % 2] = cnt

print(sum(sum(dp[i]) for i in range(4)))
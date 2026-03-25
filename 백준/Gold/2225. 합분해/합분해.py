import sys
input = sys.stdin.readline

MOD = 10 ** 9
n, k = map(int, input().split())

# dp[p][q] : 정수 p개의 합이 q가 되는 경우의 수
dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(n + 1):
    dp[1][i] = 1

for i in range(1, k):
    for j in range(n + 1):
        for t in range(j, n + 1):
            dp[i + 1][t] = (dp[i + 1][t] + dp[i][j]) % MOD

print(dp[k][n])
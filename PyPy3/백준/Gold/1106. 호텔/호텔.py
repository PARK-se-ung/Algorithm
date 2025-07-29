import sys
input = sys.stdin.readline

c, n = map(int, input().split(' '))
data = [tuple(map(int, input().split(' '))) for _ in range(n)]
dp = [10 ** 5] * (c + 100)
dp[0] = 0
for i in range(n):
    for j in range(data[i][1], c + 100):
        dp[j] = min(dp[j], dp[j - data[i][1]] + data[i][0])
print(min(dp[c:]))

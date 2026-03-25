import sys
input = sys.stdin.readline

k, n = map(int, input().split())

def func(k, n):
    if k == 0: return 0
    if k == n: return (1 << n) - 1

    # dp[p][q] : p초후 위치가 수면아래 qcm인 경우의 수
    dp = [[0] * (k + n + 1) for _ in range(n + 1)]
    dp[0][k] = 1
    for i in range(n):
        for j in range(1, k + n + 1):
            if j < k + n:
                dp[i + 1][j + 1] += dp[i][j]
            if j > 1:
                dp[i + 1][j - 1] += dp[i][j]
    
    return sum(dp[n][t] for t in range(1, k + n + 1))

print(func(k, n))
import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
dp = [0] * (m + 1)
for _ in range(n):
    v, c, k = map(int, input().split(' '))
    current = 1
    while k > 0:
        if v * current > m: break
        for i in range(m, v * current - 1, -1):
            dp[i] = max(dp[i], dp[i - v * current] + c * current)
        k -= current
        current *= 2
        if current > k:
            for i in range(m, v * k - 1, -1):
                dp[i] = max(dp[i], dp[i - v * k] + c * k)
            break
        
print(max(dp))
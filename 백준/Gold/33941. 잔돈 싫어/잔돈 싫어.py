import sys
input = sys.stdin.readline

n = int(input())
dp = [-1 for _ in range(50)]
dp[0] = 0
for _ in range(n):
    c = int(input())
    copy = dp[:]
    if 500 < c < 20000:
        for i in range(50):
            if copy[i] >= 0:
                current = copy[i] + c - 500
                dp[(current % 500) // 10] = max(dp[(current % 500) // 10], current)

print(dp[0])
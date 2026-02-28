import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
dp = [0] * 30001
arr = defaultdict(list)

for _ in range(n):
    s, e = map(int, input().split())
    arr[e].append(s)

prev = 0
for e in range(30001):
    dp[e] = prev
    if e in arr:
        for s in arr[e]:
            dp[e] = max(dp[e], dp[s] + e - s)
    prev = dp[e]

print(dp[-1])
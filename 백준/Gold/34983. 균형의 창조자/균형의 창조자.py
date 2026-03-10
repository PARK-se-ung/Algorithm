import sys
input = sys.stdin.readline

n, ri, rg = map(int, input().split())
dp = [[float('inf')] * (rg + 1) for _ in range(ri + 1)]
dp[0][0] = 0

arr = [tuple(map(int, input().split())) for _ in range(n)]

for vi, vg in arr:
    for i in range(ri, -1, -1):
        for g in range(rg, -1, -1):
            if dp[i][g] != float('inf'):
                dp[min(ri, i + vi)][min(rg, g + vg)] = min(dp[min(ri, i + vi)][min(rg, g + vg)], dp[i][g] + 1)

print(-1) if dp[ri][rg] == float('inf') else print(dp[ri][rg]) 
import sys
input = sys.stdin.readline

def dist(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5

while True:
    n = int(input())
    if n == 0: break

    targets = [(0, 0, 0)]
    for _ in range(n):
        targets.append(tuple(map(int, input().split())))
    targets.append((100, 100, 0))

    prefix = [0] * (n + 2)

    for i in range(n):
        prefix[i + 1] = prefix[i] + targets[i + 1][2]

    dp = [float('inf')] * (n + 2)
    dp[0] = 0

    for i in range(1, n + 2):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + dist(targets[i], targets[j]) + prefix[i - 1] - prefix[j] + 1)

    print(f"{dp[n + 1]:.3f}")
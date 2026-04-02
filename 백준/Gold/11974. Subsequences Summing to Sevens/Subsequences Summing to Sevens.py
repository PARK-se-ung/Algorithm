import sys
input = sys.stdin.readline

n = int(input())
prefix = [0]
for i in range(n):
    prefix.append((prefix[-1] + int(input())) % 7)

M = 0
memo = [[] for _ in range(7)]
for i in range(n + 1):
    if prefix[i] == 0: M = max(M, i)
    else:
        if len(memo[prefix[i]]) >= 2: memo[prefix[i]].pop()
        memo[prefix[i]].append(i)

for i in range(1, 7):
    if len(memo[i]) == 2:
        M = max(M, memo[i][1] - memo[i][0])

print(M)
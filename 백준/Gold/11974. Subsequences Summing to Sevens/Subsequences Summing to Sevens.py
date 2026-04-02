import sys
input = sys.stdin.readline

n = int(input())
prefix = [0]
for i in range(n):
    prefix.append((prefix[-1] + int(input())) % 7)

M = 0
memo = [-1] * 7
for i in range(n + 1):
    if memo[prefix[i]] == -1: memo[prefix[i]] = i
    else: M = max(M, i - memo[prefix[i]])

print(M)
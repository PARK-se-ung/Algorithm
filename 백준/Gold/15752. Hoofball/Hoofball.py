import sys
input = sys.stdin.readline

n = int(input())
cows = list(map(int, input().split()))

if n <= 2:
    print(1)
    sys.exit(0)

cows.sort()

degree = [0] * n
degree[1] = degree[n - 2] = 1

next = [None] * n
next[0], next[n - 1] = 1, -1

for i in range(1, n - 1):
    left, right = cows[i] - cows[i - 1], cows[i + 1] - cows[i]

    if left <= right: 
        degree[i - 1] += 1
        next[i] = -1
    else: 
        degree[i + 1] += 1
        next[i] = 1

visited = [False] * n

result = 0
for i in range(n):
    if degree[i] == 0:
        idx = i
        while not visited[idx]:
            visited[idx] = True
            idx = idx + next[idx]
        result += 1

print(result + sum(1 for v in visited if not v) // 2)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
stuff = [tuple(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(m)]

knapsack = [0] * (1000001)

for i in range(n):
    w, v = stuff[i]
    for j in range(10 ** 6, w - 1, -1):
        knapsack[j] = max(knapsack[j], knapsack[j - w] + v)

result = 1
efficient = (0, 1)

for i in range(m):
    if efficient[0] * bag[i] < knapsack[bag[i]] * efficient[1]:
        efficient = (knapsack[bag[i]], bag[i])
        result = i + 1

print(result)
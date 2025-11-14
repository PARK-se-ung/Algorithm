import sys
input = sys.stdin.readline

n, t = map(int, input().split())
A = list(map(lambda x : int(x) - 1, input().split()))

cycle = [0] * n
cycle[0] = 1

x = 0
idx, period = -1, 0
for i in range(t):
    idx = i + 1
    if cycle[A[x]] == 0:
        cycle[A[x]] = cycle[x] + 1
        x = A[x]
    else:
        period = cycle[x] - cycle[A[x]] + 1
        x = A[x]
        break

if idx < t:
    r = (t - idx) % period
    for i in range(r):
        x = A[x]

print(x + 1)
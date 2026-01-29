import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
order = dict()
for i in range(n):
    if arr[i] not in order:
        order[arr[i]] = i

for _ in range(m):
    d = int(input())
    print(order[d]) if d in order else print(-1)

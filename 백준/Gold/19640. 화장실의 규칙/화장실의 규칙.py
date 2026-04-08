import sys
input = sys.stdin.readline
from collections import deque
import heapq

n, m, k = map(int, input().split())
memo = [deque([]) for _ in range(m)]
for i in range(n):
    d, h = map(int, input().split())
    memo[i % m].append((-d, -h, i % m, i))

heap = []
for i in range(m):
    if memo[i]: heapq.heappush(heap, memo[i].popleft())

for t in range(n):
    d, h, l, i = heapq.heappop(heap)
    if i == k:
        print(t)
        break
    if memo[l]:
        heapq.heappush(heap, memo[l].popleft())

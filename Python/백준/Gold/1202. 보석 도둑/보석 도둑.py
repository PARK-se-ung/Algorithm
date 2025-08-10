import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split(' '))
jewel = [list(map(int, input().split(' '))) for _ in range(n)]
backpack = [int(input()) for _ in range(k)]

jewel.sort(key = lambda x : x[0])
backpack.sort()

heap = []
idx = 0

result = 0
for bag in backpack:
    while idx < n and jewel[idx][0] <= bag:
        heapq.heappush(heap, -jewel[idx][1])
        idx += 1
    if heap:
        result += -heapq.heappop(heap)
    
print(result)
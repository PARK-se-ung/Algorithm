import sys
input = sys.stdin.readline
import heapq

n = int(input())
lecture = [tuple(map(int, input().split())) for _ in range(n)]
lecture.sort(key = lambda x : (x[0], x[1]))

heap = [lecture[0][1]]
result = 1
for i in range(1, n):
    minimal = heapq.heappop(heap)
    if minimal > lecture[i][0]:
        heapq.heappush(heap, minimal)
    heapq.heappush(heap, lecture[i][1])
    result = max(result, len(heap))

print(result)    
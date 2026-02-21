import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque([i + 1 for i in range(n)])

result = 0
for i in range(m):
    bias = 0
    while queue[0] != arr[i]:
        bias += 1
        queue.append(queue.popleft())
    queue.popleft()
    result += min(bias, n - i - bias)

print(result)
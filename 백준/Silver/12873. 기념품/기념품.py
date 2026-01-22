import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque([i for i in range(1, n + 1)])
t = 1

result = -1

while queue:
    for i in range((t ** 3 - 1) % n):
        queue.append(queue.popleft())
    result = queue.popleft()
    t += 1
    n -= 1

print(result)
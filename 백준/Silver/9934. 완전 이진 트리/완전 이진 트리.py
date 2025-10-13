import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
seq = list(map(int, input().split()))

n = (1 << k) - 1
queue = deque([(n // 2, 1)])

result = []

while queue:
    idx, depth = queue.popleft()
    result.append(seq[idx])
    if depth == k: continue
    queue.append((idx - (1 << (k - 1 - depth)), depth + 1))
    queue.append((idx + (1 << (k - 1 - depth)), depth + 1))


for i in range(k):
    print(' '.join(map(str, result[-1 + (1 << i): -1 + (1 << i + 1)])))
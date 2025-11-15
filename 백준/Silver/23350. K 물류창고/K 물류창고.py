import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

container = deque([])
priority = [0] * m

for _ in range(n):
    p, w = map(int, input().split())
    priority[p - 1] += 1
    container.append((p - 1, w))

stack = []
result = 0
current = m - 1

while container:
    p, w = container.popleft()

    if p < current:
        container.append((p, w))
        result += w
        continue

    temp = []
    while stack:
        if stack[-1][0] == current and stack[-1][1] < w:
            tp, tw = stack.pop()
            result += tw
            temp.append((tp, tw))
        else:
            break
    stack.append((p, w))
    result += w
    while temp:
        tp, tw = temp.pop()
        stack.append((tp, tw))
        result += tw

    priority[p] -= 1
    if priority[p] == 0:
        current -= 1

print(result)
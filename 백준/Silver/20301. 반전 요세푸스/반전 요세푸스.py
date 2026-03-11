import sys
input = sys.stdin.readline
from collections import deque

n, k, m = map(int, input().split())
structure = deque([i + 1 for i in range(n)])
stack = []

flag = True
x = 0
move = 1

while structure:
    if flag: 
        t = structure.popleft()
        if move % k != 0: structure.append(t)
        else: stack.append(t)
    else:
        t = structure.pop()
        if move % k != 0: structure.appendleft(t)
        else: stack.append(t)
    move += 1

    if len(stack) % m == 0 and len(stack) != x:
        flag = not flag
        x = len(stack)

print(*stack, sep = '\n')
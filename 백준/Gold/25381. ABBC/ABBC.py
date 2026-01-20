import sys
input = sys.stdin.readline
from collections import deque

arr = list(input().rstrip())
n = len(arr)

queue = deque([])

a, b, c = 0, 0, 0

for i in range(n):
    if arr[i] == 'C':
        if b > 0:
            c += 1
    else:
        if arr[i] == 'B':
            b += 1
        queue.append(arr[i])

result, b = c, c

while queue:
    current =  queue.popleft()
    if current == 'A':
        a += 1
    else:
        if b > 0:
            b -= 1
        else:
            if a > 0:
                a -= 1
                result += 1

print(result)
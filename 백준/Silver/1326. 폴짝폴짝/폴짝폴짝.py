import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
bridge = list(map(int, input().rstrip().split(' ')))
a, b = map(int, input().rstrip().split(' '))

visited = [-1] * n
queue = deque([a - 1])
visited[a - 1] = 0

while queue:
    current = queue.popleft()
    left_current, right_current = current - bridge[current], current + bridge[current]
    l, r = 1, 1
    while left_current >= 0:
        if visited[left_current] == -1:
            visited[left_current] = visited[current] + 1
            queue.append(left_current)
        else:
            visited[left_current] = min(visited[left_current], visited[current] + 1)
        left_current -= bridge[current]
    while right_current < n:
        if visited[right_current] == -1:
            visited[right_current] = visited[current] + 1
            queue.append(right_current)
        else:
            visited[right_current] = min(visited[right_current], visited[current] + 1)
        right_current += bridge[current]

print(visited[b - 1])
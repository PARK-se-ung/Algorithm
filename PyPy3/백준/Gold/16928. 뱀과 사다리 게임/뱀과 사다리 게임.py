import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split(' '))
road = dict()
for _ in range(n + m):
    s, e = map(int, input().split(' '))
    road[s] = e
memo = [float('inf')] * 101
queue = deque([1])
memo[1] = 0

while queue:
    prev = queue.popleft()
    for i in range(1, 7, 1):
        current = prev + i
        if 1 <= current <= 100:
            if road.get(current) is not None:
                if memo[road.get(current)] == float('inf'):
                    queue.append(road.get(current))
                    memo[road.get(current)] = memo[prev] + 1
            elif memo[current] == float('inf'):
                queue.append(current)
                memo[current] = memo[prev] + 1

print(memo[100])
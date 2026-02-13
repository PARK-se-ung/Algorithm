import sys
input = sys.stdin.readline
from collections import deque

v, e = map(int, input().split())
adj = [[] for _ in range(v)]
for _ in range(e):
    v1, v2 = map(lambda x : int(x) - 1, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

flag = True
rest = v - 2
point, tail = -1, -1

for i in range(v):
    if len(adj[i]) == 1:
        if tail == -1:
            tail = i
        else:
            flag = False
            break
    elif len(adj[i]) == 2:
        if rest > 0:
            rest -= 1
        else:
            flag = False
            break
    elif len(adj[i]) == 3:
        if point == -1:
            point = i
        else:
            flag = False
            break
    else:
        flag = False
        break

if not flag or point == -1 or point == -1:
    print('NO')
    sys.exit()

queue = deque([tail])
visited = [False] * v
visited[tail] = True
cnt = 0
while queue:
    current = queue.popleft()
    cnt += 1
    for next in adj[current]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True

if cnt == v:
    print('YES')
else:
    print('NO')
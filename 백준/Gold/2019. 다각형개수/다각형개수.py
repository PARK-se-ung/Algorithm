import sys
input = sys.stdin.readline
from collections import defaultdict

e = int(input())
node = set()
adj = defaultdict(list)
prev = set()
duplicate = set()

for _ in range(e):
    x1, y1, x2, y2 = map(int, input().split())
    n1, n2 = (x1, y1), (x2, y2)
    if (n1, n2) in prev or (n2, n1) in prev:
        duplicate.add(n1)
        duplicate.add(n2)
    else:
        prev.add((n1, n2))
        prev.add((n2, n1))
    node.add(n1)
    node.add(n2)
    adj[n1].append(n2)
    adj[n2].append(n1)

v = len(node)
visited = {nd:False for nd in node}

result = 0

for nd in node:
    if not visited[nd]:
        flag = True
        stack = [nd]
        visited[nd] = True
        while stack:
            current = stack.pop()
            if len(adj[current]) != 2:
                flag = False
            for next in adj[current]:
                if next == current:
                    flag = False
                if not visited[next]:
                    stack.append(next)
                    visited[next] = True
        if flag:
            result += 1

print(result)
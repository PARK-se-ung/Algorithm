import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split(' ')))
t = int(input())

adj = [[] for _ in range(n)]
root = -1
for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        adj[parent[i]].append(i)

leaf = [0] * n

def find(num):
    if not adj[num]:
        leaf[num] = 1
        return 
    for son in adj[num]:
        if leaf[son] == 0:
            find(son)
        leaf[num] += leaf[son]

find(root)
if len(adj[parent[t]]) == 1:
    print(leaf[root] - leaf[t] + 1)
else:
    print(leaf[root] - leaf[t])
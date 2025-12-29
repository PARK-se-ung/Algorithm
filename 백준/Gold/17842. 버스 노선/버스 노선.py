import sys
input = sys.stdin.readline

n = int(input())

adj = [[] for _ in range(n)]

for i in range(n - 1):
    s, e = map(lambda x : int(x) - 1, input().split())
    adj[s].append(e)
    adj[e].append(s)

result = sum(1 for elem in adj if len(elem) == 1)
print((result + 1) // 2)
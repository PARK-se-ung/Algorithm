import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4 + 1)

def dfs1(parent, current):
    for next in adj[current]:
        if next != parent:
            s, w = dfs1(current, next)
            S[current] += s
            W[current] += w
    if parent == -1: return -1, -1
    return S[current], W[current] + S[current] * adj[current][parent]

def dfs2(parent, current):
    for next in adj[current]:
        if next != parent:
            W[next] += W[current] - W[next] - S[next] * adj[current][next] + (S[current] - S[next]) * adj[current][next]
            S[next] += S[current] - S[next]
            dfs2(current, next)

while True:
    n = int(input())
    if n == 0: break
    
    # adjust list with dictionary
    adj = [dict() for _ in range(n)]
    for i in range(n - 1):
        s, e, w = map(int, input().split(' '))
        adj[s][e] = w
        adj[e][s] = w

    # Weight, Size memoization
    W, S = [0] * n, [1] * n
    dfs1(-1, 0)
    dfs2(-1, 0)

    print(min(W))

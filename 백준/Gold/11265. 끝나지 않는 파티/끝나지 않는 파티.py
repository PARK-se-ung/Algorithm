import sys
input = sys.stdin.readline

def floyd_warshall(graph):
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

n, m = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]

dist = floyd_warshall(graph)

for _ in range(m):
    i, j, distance = map(int, input().split(' '))
    if dist[i- 1][j - 1] <= distance:
        print('Enjoy other party')
    else:
        print('Stay here')
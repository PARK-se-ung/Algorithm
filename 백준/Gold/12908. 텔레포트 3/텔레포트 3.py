import sys
input = sys.stdin.readline

start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

# nodes list
nodes = [start]

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    nodes.append((x1, y1))
    nodes.append((x2, y2))

nodes.append(end)

# adjacent matrix
adj = [[0] * 8 for _ in range(8)]

def taxi_cab(nodes, i, j):
    teleports = {
            (1, 2), (2, 1),
            (3, 4), (4, 3),
            (5, 6), (6, 5)
        }
    if (i, j) in teleports: return 10
    return abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])

for i in range(8):
    for j in range(8):
        if i != j:
            adj[i][j] = taxi_cab(nodes, i, j)

# ployd-warshall
for k in range(8):
    for i in range(8):
        for j in range(8):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

print(adj[0][7])
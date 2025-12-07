import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(lambda x : int(x) - 1, input().split())
    adj[u].append(v)
    adj[v].append(u)

color = list(input().rstrip())
visited = [False] * n

result = 0

for i in range(n):
    if not visited[i] and color[i] == 'R':
        r_size, b_size = 1, 0

        visited[i] = True
        stack = [i]

        while stack:
            current = stack.pop()

            for next in adj[current]:

                if not visited[next] and color[next] == 'R':
                    visited[next] = True
                    r_size += 1
                    stack.append(next)

                elif color[next] == 'B':
                    b_size += 1

        result += b_size * r_size

print(result)
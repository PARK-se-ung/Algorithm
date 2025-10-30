import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(lambda x : int(x) - 1, input().split()))
visited = [False] * 9
adj = [[None] * 9 for _ in range(9)]

for i in range(3):
    adj[i][i + 6], adj[i + 6][i] = i + 3, i + 3
    adj[3 * i][3  * i + 2], adj[3 * i + 2][3  * i] = 3 * i + 1, 3 * i + 1
adj[0][8], adj[8][0] = 4, 4
adj[2][6], adj[6][2] = 4, 4

result = 'YES'

visited[arr[0]] = True
prev = arr[0]

for i in range(1, n):
    if not visited[arr[i]] and (adj[prev][arr[i]] is None or visited[adj[prev][arr[i]]]):
        visited[arr[i]] = True
        prev = arr[i]
    else:
        result = 'NO'
        break

print(result)
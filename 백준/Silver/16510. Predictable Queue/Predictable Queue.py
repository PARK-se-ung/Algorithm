import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# (value, order)
query = [(int(input()), i) for i in range(m)]
query.sort(key = lambda x : x[0])

current = 0
results = [(n, -1) for _ in range(m)]

idx = -1
for i in range(m):
    while current <= query[i][0] and idx < n:
        idx += 1
        if idx == n: break
        current += arr[idx]
    results[i] = (idx, query[i][1])

results.sort(key = lambda x : x[1])

print('\n'.join(map(lambda x : str(x[0]), results)))
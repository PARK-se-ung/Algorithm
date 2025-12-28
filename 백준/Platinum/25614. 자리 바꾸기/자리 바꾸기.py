import sys
input = sys.stdin.readline

n, m = input().split()
n = int(n)
arr = list(map(lambda x : int(x) - 1, input().split()))

result = [0] * n
visited = [False] * n

def get_diff(m, p):
    if p == 1: return 0
    diff = 0
    for str in m:
        diff = (diff * 10 + int(str)) % p
    return diff

memo = dict()

for i in range(n):
    if not visited[i]:
        current = i
        cycle = []
        while not visited[current]:
            cycle.append(current)
            visited[current] = True
            current = arr[current]
        p = len(cycle)
        if memo.get(p) is None:
            memo[p] = get_diff(m, p)
        diff = memo[p]
        for i in range(p):
            result[cycle[i]] = 1 + cycle[(i + diff) % p]

print(' '.join(map(str, result)))
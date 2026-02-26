import sys
input = sys.stdin.readline
from itertools import permutations
from collections import Counter

n, m = map(int, input().split())
duration = list(map(int, input().split()))
task = []
for _ in range(m):
    t = list(map(lambda x : int(x) - 1, input().split()))
    task.append(set(t[1:]))

order = list(permutations(range(m)))

ans = n * m
for o in order:
    result = 0
    cnt = Counter()
    for i in o:
        for j in range(n):
            cnt[j] -= 1
            if j in task[i] and cnt[j] <= 0:
                cnt[j] = duration[j]
                result += 1
    ans = min(ans, result)

print(ans)
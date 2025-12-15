import sys
input = sys.stdin.readline
from collections import Counter

p = int(input())
arr = list(input().rstrip())
result = float('inf')
for t in range(1, p + 1):
    temp = 0
    for i in range(t):
        cnt = Counter()
        for j in range(i, len(arr), t):
            cnt[arr[j]] += 1
        temp += sum(cnt[key] for key in cnt) - max(cnt[key] for key in cnt)
    result = min(result, temp)
print(result)
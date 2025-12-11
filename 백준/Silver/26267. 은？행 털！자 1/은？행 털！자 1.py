import sys
input = sys.stdin.readline
from collections import Counter

result = Counter()
for _ in range(int(input())):
    x, t, c = map(int, input().split())
    result[t - x] += c

print(max(result[key] for key in result))
import sys
input = sys.stdin.readline
from collections import Counter

A, B, C, D = [], [], [], []
for _ in range(int(input())):
    a, b, c, d = map(int, input().split(' '))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

cnt = Counter()

for a in A:
    for b in B:
        cnt[a + b] += 1
result = 0
for c in C:
    for d in D:
        result += cnt[- c - d]

print(result)
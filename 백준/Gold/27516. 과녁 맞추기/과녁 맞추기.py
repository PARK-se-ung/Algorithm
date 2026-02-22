import sys
input = sys.stdin.readline
from collections import Counter

bx, by = map(int, input().split())
n = int(input())

left, right = [], []
for _ in range(n):
    x, y = map(int, input().split())
    coord = (x - bx, y - by)
    if y - by < 0:
        if x - bx > 0:
            right.append(coord)
        elif x - bx < 0:
            left.append(coord)

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

def func(arr):
    cnt = Counter()
    for elem in arr:
        x, y = elem[0] ** 2, -elem[1]
        g = gcd(x, y)
        cnt[(x // g, y // g)] += 1

    result = 0
    for key in cnt:
        result = max(result, cnt[key])
    
    return result

print(max(func(left), func(right)))

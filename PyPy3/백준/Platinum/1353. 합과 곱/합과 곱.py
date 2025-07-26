import sys
input = sys.stdin.readline
import math

s, p = map(int, input().split(' '))
e = math.e
n = math.floor(s / e)
ans = -1

if s == p:
    ans = 1
elif s > p:
    ans = 2
else:
    for i in range(1, s + 1):
        if s ** i >= p * (i ** i):
            ans = i
            break
        elif i > n + 1:
            break
print(ans)
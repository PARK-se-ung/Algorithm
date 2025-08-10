import sys
input = sys.stdin.readline
import math
x, y, d, t = map(int, input().split(' '))
l = math.sqrt(x ** 2 + y ** 2)
if d <= t:
    print(l)
else:
    if l >= d:
        print(t * (l // d) + min(t, l % d))
    else:
        print(min(2 * t, l, t + d - l))
import sys
input = sys.stdin.readline
import math

for _ in range(int(input())):
    raw = input().rstrip()
    n = int(raw)
    an = int(raw[::-1])
    if math.isqrt(n) == math.sqrt(n) and math.isqrt(an) == math.sqrt(an):
        print('YES')
    else:
        print('NO')


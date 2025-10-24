import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    base = sum(float(input()) * 100 for _ in range(n)) / 100
    spec = list()
    for f in range(10 ** 4 + 1):
        price = base * (1 + f / 100)
        upper = math.ceil(price * 100) / 100
        lower = math.floor(price * 100) / 100
        if math.floor(upper) == x or math.floor(lower) == x:
            spec.append(f)
    print(f'{min(spec)} {max(spec)}')
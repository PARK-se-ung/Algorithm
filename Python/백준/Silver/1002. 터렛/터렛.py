import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    c1, c2 = (x1, y1), (x2, y2)
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if c1 != c2:
        if d > (r1 + r2) ** 2 or d < (r1 - r2) ** 2:
            print(0)
        elif d == (r1 + r2) ** 2 or d == (r1 - r2) ** 2:
            print(1)
        else:
            print(2)
    else: # c1 == c2
        if r1 == r2:
            print(-1)
        else:
            print(0)
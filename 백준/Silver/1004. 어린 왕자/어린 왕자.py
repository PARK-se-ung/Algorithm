import sys
input = sys.stdin.readline

def checker(x, y, cx, cy, r):
    if (x - cx) ** 2 + (y - cy) ** 2 < r ** 2:
        return 1
    return 0

for _ in range(int(input())):
    x0, y0, x1, y1 = map(int, input().split())
    n = int(input())
    result = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        if checker(x0, y0, cx, cy, r) + checker(x1, y1, cx, cy, r) == 1:
            result += 1
    print(result)


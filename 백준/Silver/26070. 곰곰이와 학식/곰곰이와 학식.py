import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

result = 0

while a * x > 0 or b * y > 0 or c * z > 0 or x >= 3 or y >= 3 or z >= 3:
    p = min(a, x)
    a, x = a - p, x - p
    result += p
    y += x // 3
    x %= 3

    q = min(b, y)
    b, y = b - q, y - q
    result += q
    z += y // 3
    y %= 3

    r = min(c, z)
    c, z = c - r, z - r
    result += r
    x += z // 3
    z %= 3

print(result)
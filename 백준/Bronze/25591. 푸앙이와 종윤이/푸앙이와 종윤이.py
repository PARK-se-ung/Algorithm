import sys
input = sys.stdin.readline

x, y = map(int, input().split())

a, b = 100 - x, 100 - y
c, d = 100 - (a + b), a * b
q = d // 100
r = d % 100

print(f'{a} {b} {c} {d} {q} {r}')
print(f'{c + q} {r}')
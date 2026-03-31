import sys
input = sys.stdin.readline

r, g, b = map(lambda x : int(x) / 255, input().split())
m = max(r, g, b)
result = []
if m == 0:
    result = [0, 0, 0, 1]
else:
    result = [(m - r) / m, (m - g) / m, (m - b) / m, 1 - m]
print(*result)
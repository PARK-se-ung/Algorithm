import sys
input = sys.stdin.readline

INF = 10 ** 18

def func(x):
    result = []
    current = 1
    while current < INF:
        result.append(current)
        current *= x
    return result

a, b, c, idx = map(int, input().split())
A, B, C = func(a), func(b), func(c)

result = []

for i in A:
    for j in B:
        for k in C:
            result.append(i * j * k)

result.sort()

print(result[idx])
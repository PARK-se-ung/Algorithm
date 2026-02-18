import sys
input = sys.stdin.readline

n = int(input())

def build(n):
    if n % 2 == 1:
        return build(n - 1) + [n]
    result = []
    t = n // 2
    for i in range(1, t + 1):
        result.append(t + i)
        result.append(t + 1 - i)
    return result

print(' '.join(map(str, build(n))))
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, d, a, b, f = map(float, input().split())
    print(f'{n} {f * d / (a + b)}')
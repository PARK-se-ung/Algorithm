import sys
input = sys.stdin.readline

n, m, s = map(int, input().split())
print(min((m + 1) * (100 - n) * s // 100, m * s))
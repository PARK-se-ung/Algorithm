import sys
input = sys.stdin.readline
m, d = map(int, input().split())
print((d + m - 1) // m)
import sys
input = sys.stdin.readline

a, t = map(int, input().split())
print(max(0, 60 + 2 * (t - a)))
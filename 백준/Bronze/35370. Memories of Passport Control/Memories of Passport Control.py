import sys
input = sys.stdin.readline

k, s = map(int, input().split())
print(s // k + s % k)
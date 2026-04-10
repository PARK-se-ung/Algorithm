import sys
input = sys.stdin.readline

x, d = map(int, input().split())
print("double it") if 2 * x <= d else print("take it")
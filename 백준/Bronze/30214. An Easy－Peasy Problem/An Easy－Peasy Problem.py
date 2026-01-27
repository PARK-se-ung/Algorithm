import sys
input = sys.stdin.readline

a, b = map(int, input().split())
print('E') if a * 2 >= b else print('H')
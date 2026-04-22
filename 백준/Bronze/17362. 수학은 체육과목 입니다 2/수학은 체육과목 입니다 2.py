import sys
input = sys.stdin.readline

n = int(input()) % 8
if n == 0: n = 8
print(n) if n <= 5 else print(10 - n)
import sys
input = sys.stdin.readline

n = int(input())
print(1) if n // 10 == n % 10 else print(0)
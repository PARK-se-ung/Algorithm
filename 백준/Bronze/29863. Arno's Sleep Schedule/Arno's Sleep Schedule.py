import sys
input = sys.stdin.readline

result = -int(input()) + int(input())
print(result) if result > 0 else print(24 + result)

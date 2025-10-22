import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
result = 0
prev = -1
for i in range(n - 1, -1, -1):
    if arr[i] > prev:
        result += 1
        prev = arr[i]
print(result)
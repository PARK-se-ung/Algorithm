import sys
input = sys.stdin.readline

n = int(input())

result = 1
for i in range(1, n):
    result += n / i

print(result)
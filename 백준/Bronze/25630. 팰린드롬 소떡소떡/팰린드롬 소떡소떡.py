import sys
input = sys.stdin.readline

n = int(input())
str = input().rstrip()
result = 0
for i in range(n // 2):
    if str[i] != str[n - 1 - i]:
        result += 1

print(result)
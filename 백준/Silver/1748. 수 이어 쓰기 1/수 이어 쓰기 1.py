import sys
input = sys.stdin.readline

n = int(input())
result = 0
digit = 1
num = 9
while n > 0:
    result += digit * min(num, n)
    n -= num
    digit += 1
    num *= 10

print(result)
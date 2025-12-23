import sys
input = sys.stdin.readline

result = 0

for _ in range(int(input())):
    result += int(input()) % 2

print(result)

import sys
input = sys.stdin.readline

str = list(input().rstrip())
targets = {'a', 'e', 'i', 'o', 'u'}
result = 0
for elem in str:
    if elem in targets:
        result += 1
print(result)
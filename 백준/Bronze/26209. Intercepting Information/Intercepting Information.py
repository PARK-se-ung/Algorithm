import sys
input = sys.stdin.readline

seq = list(map(int, input().split(' ')))
result = 'S'

for elem in seq:
    if elem == 9:
        result = 'F'
        break

print(result)
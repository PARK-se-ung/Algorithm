import sys
input = sys.stdin.readline

s = {'A', 'a', 'b', 'D', 'd', 'e', 'g', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', '@'}
result = 0
for elem in input().rstrip():
    if elem in s: result += 1
    elif elem == 'B': result += 2

print(result)
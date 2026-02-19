import sys
input = sys.stdin.readline

n = int(input())
temp = list(input().split())
origin = {temp[i]:0 for i in range(n)}
ingredient = list(input().split())
for elem in ingredient:
    origin[elem] = 1

for elem in temp:
    if origin[elem] == 0:
        print(elem)
        break
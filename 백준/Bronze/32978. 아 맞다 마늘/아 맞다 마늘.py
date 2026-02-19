import sys
input = sys.stdin.readline

n = int(input())
origin = list(input().split())
ingredient = set(input().split())
for elem in origin:
    if elem not in ingredient:
        print(elem)
        break
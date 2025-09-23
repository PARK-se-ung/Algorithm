import sys
input = sys.stdin.readline

n = int(input())
w, v = map(int, input().split())
print(1 if n * v <= w else 0)
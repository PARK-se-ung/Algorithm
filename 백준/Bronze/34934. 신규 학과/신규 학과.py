import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, y = input().split()
    if int(y) == 2026:
        print(n)
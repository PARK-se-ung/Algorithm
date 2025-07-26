import sys
input = sys.stdin.readline

n = int(input())
r, c = map(lambda x : int(x) - 1, input().split(' '))
if n == 3:
    if r == c == 1: print(1)
    else: print(4)
else:
    if (r + c) % 2 == 0 and n % 2 == 1:
        print(n ** 2 // 2 + 1)
    else:
        print(n ** 2 // 2)
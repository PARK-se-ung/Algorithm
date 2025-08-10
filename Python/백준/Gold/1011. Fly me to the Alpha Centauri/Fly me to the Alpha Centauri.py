import sys
input = sys.stdin.readline

def square(x):
    s = 0
    while s ** 2 < x:
        s += 1
    return s - 1 if s ** 2 != x else s

for _ in range(int(input())):
    x, y = map(int, input().split(' '))
    n = y - x
    root = square(n)
    if n == root ** 2:
        print(2 * root - 1)
    elif n <= root ** 2 + root:
        print(2 * root)
    else:
        print(2 * root + 1)

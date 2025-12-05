import sys
input = sys.stdin.readline

n, m = map(int, input().split())


if n == 1:
    if m == 0:
        print(1)
    else:
        print(2)
elif n == 2:
    if m == 0:
        print(1)
    elif m == 1:
        print(3)
    else:
        print(4)
else:
    total, even, odd, third = n, n // 2, (n + 1) // 2, (n + 2) // 3
    if m < third:
        print(1)
    elif m < even:
        print(2)
    elif m < odd:
        print(3)
    elif m < even + third:
        print(4)
    elif m < odd + third:
        print(5)
    elif m < total:
        print(6)
    elif m < total + third:
        print(7)
    else:
        print(8)
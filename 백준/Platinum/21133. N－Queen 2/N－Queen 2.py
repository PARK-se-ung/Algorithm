import sys
input = sys.stdin.readline

n = int(input())

arr = []

if n % 6 == 2:
    for i in range(n // 2):
        arr.append(2 * i + 2)
    arr.append(3)
    arr.append(1)
    for i in range(n // 2 - 3):
        arr.append(2 * i + 7)
    arr.append(5)
elif n % 6 == 3:
    for i in range(n // 2 - 1):
        arr.append(2 * i + 4)
    arr.append(2)
    for i in range(n // 2 - 1):
        arr.append(2 * i + 5)
    arr.append(1)
    arr.append(3)
elif n % 2 == 0:
    for i in range(n):
        if i < n // 2:
            arr.append(2 * i + 2)
        else:
            arr.append(2 * (i - n // 2) + 1)
else:
    for i in range(n):
        if i <= n // 2:
            arr.append(2 * i + 1)
        else:
            arr.append(2 * (i - n // 2))

print('\n'.join(map(str, arr)))
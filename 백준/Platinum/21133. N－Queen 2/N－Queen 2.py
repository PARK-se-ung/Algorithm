import sys
input = sys.stdin.readline

n = int(input())

arr = []
if n % 2 == 0:
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
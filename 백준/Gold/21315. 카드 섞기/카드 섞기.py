import sys
input = sys.stdin.readline

n = int(input())
origin = tuple(range(1, n + 1))
arr = list(map(int, input().split()))

M = 1
while 2 ** M < n:
    M += 1

def func(arr, k):
    for i in range(k):
        arr = arr[2 ** i:2 ** (i + 1)] + arr[:2 ** i] + arr[2 ** (i + 1):]
    return arr[2 ** k:] + arr[:2 ** k]

second = [func(arr, k) for k in range(1, M)]

for i in range(1, M):
    for j in range(1, M):
        if tuple(func(second[i - 1], j)) == origin:
            print(f"{j} {i}")
            sys.exit(0)
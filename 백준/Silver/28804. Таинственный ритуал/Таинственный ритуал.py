import sys
input = sys.stdin.readline


def func(x):
    if x in {1, 2, 5, 10}:
        return 1
    if x == 4:
        return 2
    if x in {3, 6}:
        return 3
    if x == 8:
        return 4
    if x > 10:
        return func(1 + func(x % 10))
    return x

for _ in range(int(input())):
    arr = list(map(int, list(input().rstrip())))    
    while len(arr) > 1:
        last = arr.pop()
        arr[-1] += last // 10
        arr[-1] += func(last % 10)
    
    while arr[0] not in {0, 1, 3, 7, 9}:
        arr[0] = func(arr[0])
    print(arr[0])
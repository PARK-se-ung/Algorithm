import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def func(n, arr):
    for i in range(n - 1):
        if arr[i + 1] == arr[i]:
            return 0
        
    return 1

print(func(n, arr))
    
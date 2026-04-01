import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
result = [0, 0]
for i in range(2):
    arr.sort(key = lambda x : x[i])
    result[i] = arr[n // 2][i]
print(*result)
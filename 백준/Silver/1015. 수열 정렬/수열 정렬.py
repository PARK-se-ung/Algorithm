import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
temp = [(arr[i], i) for i in range(n)]
temp.sort(key = lambda x : (x[0], x[1]))
result = [-1] * n
for i in range(n):
    result[temp[i][1]] = i

print(*result)
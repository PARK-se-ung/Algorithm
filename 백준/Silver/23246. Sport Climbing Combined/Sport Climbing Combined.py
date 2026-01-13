import sys
input = sys.stdin.readline

arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key = lambda x : (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))
result = [arr[i][0] for i in range(3)]
print(' '.join(map(str, result)))
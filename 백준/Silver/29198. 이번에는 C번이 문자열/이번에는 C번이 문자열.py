import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    s = list(input().rstrip())
    s.sort()
    s = tuple(s)
    arr.append(s)

arr.sort()

result = []

for i in range(k):
    for j in range(m):
        result.append(arr[i][j])

result.sort()

print(''.join(result))
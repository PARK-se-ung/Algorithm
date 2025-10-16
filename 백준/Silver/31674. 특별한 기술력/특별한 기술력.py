import sys
input = sys.stdin.readline

div = 10 ** 9 + 7
n = int(input())
arr = list(map(int, input().split()))

arr.sort(key = lambda x: -x)

result = arr[0]

for i in range(1, n):
    result *= 2
    result += arr[i]
    result %= div

print(result)
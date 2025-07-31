import sys
input = sys.stdin.readline
n = int(input())
chain = list(map(int, input().split(' ')))
chain.sort()
result = 0
idx = 0
while n > 1:
    if chain[idx] < n - 1:
        n -= chain[idx] + 1
        result += chain[idx]
        idx += 1
    else:
        result += n - 1
        break
print(result)

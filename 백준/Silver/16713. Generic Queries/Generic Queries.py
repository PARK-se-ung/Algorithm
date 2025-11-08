import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] ^ arr[i]

result = 0

for _ in range(q):
    s, e = map(int, input().split())
    result ^= prefix[s - 1] ^ prefix[e]

print(result)
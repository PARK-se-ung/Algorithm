import sys
input = sys.stdin.readline

x, k = map(int, input().split(' '))
result = 0
idx = 0
for i in range(x.bit_length() + k.bit_length()):
    if idx == k.bit_length(): break
    if not x & (1 << i):
        if k & (1 << idx):
            result |= 1 << i
        idx += 1


print(result)

import sys
input = sys.stdin.readline

k = int(input())
length = k.bit_length()
for i in range(length):
    if k & (1 << i):
        if k == 1 << i: print(f'{1 << length - 1} {0}')
        else: print(f'{1 << length} {length - i}')
        break

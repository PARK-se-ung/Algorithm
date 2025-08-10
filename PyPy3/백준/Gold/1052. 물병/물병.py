import sys
input = sys.stdin.readline
n, k = map(int, input().split(' '))
b = n.bit_count()
if b <= k : print(0)
else:
    bits = list(map(int, bin(n)[:1:-1]))
    bits.append(0)
    result = 0
    for i in range(len(bits)):
        if b <= k: break
        if bits[i] == 1:
            result += 1 << i
            bits[i + 1] += 1
        elif bits[i] == 2:
            b -= 1
            bits[i + 1] += 1
    print(result)
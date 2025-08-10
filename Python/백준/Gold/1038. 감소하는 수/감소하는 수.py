import sys
input = sys.stdin.readline

n = int(input())
if n >= 2 ** 10 - 1:
    print(-1)
else:
    def combi(n, r):
        if n == r:
            return 1
        if r == 0:
            return 1
        else:
            return combi(n - 1, r) + combi(n - 1, r - 1)
    n += 1
    std = [0 for _ in range(11)]
    bdy = 2 ** 10 - 1
    for i in range(10, 0, -1):
        std[i] = bdy
        bdy -= combi(10, i)
    digit = 1
    while std[digit] < n:
        digit += 1
    N = n - std[digit - 1]
    S = [digit - i for i in range(digit)]
    idxout = 0
    while digit > 0:
        hockey = [combi(digit + i, digit) for i in range(11 - digit)]
        idxin = 0
        while hockey[idxin] < N:
            idxin += 1
        N -= hockey[idxin - 1]
        S[idxout] += idxin - 1
        digit -= 1
        idxout += 1
    print(''.join(map(str, S)))

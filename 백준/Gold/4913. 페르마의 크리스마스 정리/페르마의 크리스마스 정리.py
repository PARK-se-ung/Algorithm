import sys
input = sys.stdin.readline

upper = 10 ** 6
prime = [True] * upper
prime[0], prime[1] = False, False

for i in range(2, int(upper ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, upper, i):
            prime[j] = False

# [total, sum of square]
prefix = [[0, 0] for _ in range(upper)]
for i in range(2, upper):
    prefix[i][0], prefix[i][1] = prefix[i - 1][0], prefix[i - 1][1]
    if prime[i]:
        prefix[i][0] += 1
        if i % 4 == 1 or i == 2: prefix[i][1] += 1

while True:
    L, U = map(int, input().split())
    if L == -1 and U == -1: break

    result = [L, U]
    result.append(prefix[max(U, 0)][0] - prefix[max(0, L - 1)][0])
    result.append(prefix[max(U, 0)][1] - prefix[max(0, L - 1)][1])

    print(' '.join(map(str, result)))
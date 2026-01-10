import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 9

n = int(input())

if n == 1:
    print(0)
    sys.exit(0)

print(2 * pow(3, n - 2, MOD) % MOD)
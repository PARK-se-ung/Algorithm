import sys
input = sys.stdin.readline

DIV = 10007

n, k = map(int, input().split())

memo = dict()

def combination(n, k):
    if k == 0 or n == k: return 1
    if k == 1 or n - k == 1: return n
    if (n, k) in memo: return memo[(n, k)]
    
    memo[(n - 1, k)] = combination(n - 1, k)
    memo[(n - 1, k - 1)] = combination(n - 1, k - 1)

    return (combination(n - 1, k) + combination(n - 1, k - 1)) % DIV

print(combination(n, k))
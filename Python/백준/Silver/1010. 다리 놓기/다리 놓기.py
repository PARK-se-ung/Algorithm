import sys
input = sys.stdin.readline

def combi(n, k):
    c = 1
    for i in range(k):
        c *= n - i
        c //= i + 1
    return c

for _ in range(int(input())):
    k, n = map(int, input().split(' '))
    print(combi(n, k))
import sys
input = sys.stdin.readline

INF = 10 ** 9 + 7

n, m, a = map(int, input().split())
h = int(input())

print(pow(m, n - 1, INF))
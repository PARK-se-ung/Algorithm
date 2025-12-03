import sys
input = sys.stdin.readline

a, b, c = map(lambda x : abs(int(x)), input().split())
print('YES' if a + b <= c and (a + b) % 2 == c % 2 else 'NO')
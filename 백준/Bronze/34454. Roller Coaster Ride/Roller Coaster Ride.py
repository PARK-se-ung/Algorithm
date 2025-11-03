import sys
input = sys.stdin.readline

n = int(input())
c = int(input())
p = int(input())
print('yes' if n <= c * p else 'no')
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
total = sum(map(int, input().split())) - n
print('DIMI') if total >= m else print('OUT')

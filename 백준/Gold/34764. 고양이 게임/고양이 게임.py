import sys

n = int(sys.stdin.readline())
print('goose' if n % 4 < 2 else 'duck')
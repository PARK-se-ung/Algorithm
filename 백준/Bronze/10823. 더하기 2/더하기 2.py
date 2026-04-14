import sys

s = sys.stdin.read().replace('\n', '')
print(sum(map(int, s.split(','))))
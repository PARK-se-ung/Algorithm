import sys
input = sys.stdin.readline

s1, s2 = input().rstrip(), input().rstrip()
print(0 if s1 == s2 else 1550)
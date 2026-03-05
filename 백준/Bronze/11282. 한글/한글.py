import sys
input = sys.stdin.readline

n = int(input())

print(chr(0xAC00 + n - 1))
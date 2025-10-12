import sys
input = sys.stdin.readline

n = int(input())
div = 1000000007

print((3 ** n - 1) % div)
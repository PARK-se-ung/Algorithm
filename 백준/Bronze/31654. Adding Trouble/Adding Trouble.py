import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
print("correct!") if a + b == c else print("wrong!")
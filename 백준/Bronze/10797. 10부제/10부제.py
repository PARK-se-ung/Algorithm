import sys
input = sys.stdin.readline

day = int(input())
cars = list(map(int, input().split()))
result = 0
for car in cars:
    result += 1 if car % 10 == day else 0

print(result)
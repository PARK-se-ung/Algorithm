import sys
input = sys.stdin.readline

n = int(input())
ball = list(map(int, input().split(' ')))
print(2 * (max(ball) - min(ball)))
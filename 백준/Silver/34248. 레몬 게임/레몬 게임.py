import sys
input = sys.stdin.readline

# 1의 개수가 2의 개수 이상이고 2와 짝을 맞추고 남은 1의 개수가 3의 배수면 가능

n = int(input())
arr = list(map(int, input().split()))

one, two = 0, 0
for elem in arr:
    if elem == 1: one += 1
    else: two += 1

if one >= two and (one - two) % 3 == 0: print('Yes')
else: print('No')
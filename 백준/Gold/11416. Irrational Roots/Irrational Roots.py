import sys
input = sys.stdin.readline

# 최고차항이 1인 정수계수 n차 방정식의 유리근은 반드시 정수
n = int(input())
coeffi = [1] + list(map(int, input().split()))

# 근 판정
def root(coeffi, r):
    return sum(coeffi[i] * (r ** (len(coeffi) - 1 - i)) for i in range(len(coeffi))) == 0

# 조립제법
def func(coeffi, r):
    new_coeffi = [1] * n
    for i in range(1, n):
        new_coeffi[i] = coeffi[i] + r * new_coeffi[i - 1]
    return new_coeffi


result = n

while n > 0:
    for r in range(1, 11):
        if root(coeffi, r):
            result -= 1
            coeffi = func(coeffi, r)
        if root(coeffi, -r):
            result -= 1
            coeffi = func(coeffi, -r)
    n -= 1

print(result)
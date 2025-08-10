import sys
input = sys.stdin.readline

def calc(a, b):
    if a % 10 == 0:
        return 10
    if a % 10 in [1, 5, 6]:
        return a % 10
    if a % 10 == 2:
        return [6, 2, 4, 8][b % 4]
    if a % 10 == 3:
        return [1, 3, 9, 7][b % 4]
    if a % 10 == 4:
        return [6, 4][b % 2]
    if a % 10 == 7:
        return [1, 7, 9, 3][b % 4]
    if a % 10 == 8:
        return [6, 8, 4, 2][b % 4]
    if a % 10 == 9:
        return [1, 9][b % 2]

for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    print(calc(a, b))
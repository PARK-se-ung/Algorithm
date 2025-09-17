import sys
input = sys.stdin.readline

idx = 1
while True:
    n = int(input())
    if n == 0: break
    students = [input().rstrip() for _ in range(n)]

    earings = [0] * n

    for _ in range(2 * n - 1):
        x, y = input().rstrip().split(' ')
        x = int(x) - 1
        earings[x] += 1
    
    for i in range(n):
        if earings[i] < 2:
            print(f'{idx} {students[i]}')
            break
    idx += 1

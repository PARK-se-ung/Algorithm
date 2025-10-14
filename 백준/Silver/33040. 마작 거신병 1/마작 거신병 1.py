import sys
input = sys.stdin.readline

r, c = map(int, input().split())
a, b = map(int, input().split())

x = r * (r - 1) // 2
flag = a < x or b < x

if r == 1: 
    current = [1] * a + [9] * b
    print(' '.join(map(str, current)))

elif flag: print(-1)

else:
    m, n = (b - x) // r, (b - x) % r
    for i in range(r):
        current = [9] * (m + i)
        
        if i >= r - n: current.append(9)

        while len(current) < c:
            current.append(1)

        print(' '.join(map(str, current)))
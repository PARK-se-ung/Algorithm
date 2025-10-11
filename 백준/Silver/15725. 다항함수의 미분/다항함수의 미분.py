import sys
input = sys.stdin.readline

poly = input().rstrip()
if poly[0] == 'x': print(1)
elif poly[0] == '-' and poly[1] == 'x': print(-1)
else:
    flag = True
    for i in range(len(poly)):
        if poly[i] == 'x':
            print(poly[:i])
            flag = False
            break
    if flag:
        print(0)
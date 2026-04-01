import sys
input = sys.stdin.readline

n, s = map(int, input().split())
s -= 1
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
direct = 1
power = 1
infinity = False
while 0 <= s < n:
    if arr[s][0] == 1:
        if arr[s][1] <= power:
            result += 1
            arr[s][1] = float('inf')
    else:
        direct *= -1
        power += arr[s][1]
        if arr[s][1] == 0:
            if not infinity: infinity = True
            else: break
        else: infinity = False

    s += direct * power

print(result)
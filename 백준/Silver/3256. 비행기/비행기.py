import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) - 1 for _ in range(n)]

time = -1
idx = 0
line = [0] * 1000
pos = [-1] * 1000
flag = True

while flag:
    flag = False
    time += 1
    for i in range(999, -1, -1):
        if pos[i] >= 0:
            flag = True
            if i == arr[pos[i]]:
                if line[i] > 0:
                    line[i] -= 1
                    if line[i] == 0:
                        pos[i] = -1
            elif i < 999:
                if pos[i + 1] == -1:
                    pos[i + 1], line[i + 1] = pos[i], line[i]
                    line[i], pos[i] = 0, -1
    if idx < n and pos[0] == -1:
        flag = True
        pos[0] = idx
        line[0] = 5
        idx += 1

print(time - 1)
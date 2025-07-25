import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
times = list(tuple(map(int, input().split(' '))) for _ in range(n))
times.sort(key = lambda x : (x[0], x[1]))
result = 0
meeting = [0 for _ in range(k)]
for i in range(n):
    flag = True
    for j in range(k):
        if meeting[j] < times[i][0]:
            meeting[j] = times[i][1]
            result += 1
            meeting.sort()
            flag = False
            break
    if flag:
        for j in range(k - 1, -1, -1):
            if meeting[j] > times[i][1]:
                meeting[j] = times[i][1]
                meeting.sort()
                break

print(result)
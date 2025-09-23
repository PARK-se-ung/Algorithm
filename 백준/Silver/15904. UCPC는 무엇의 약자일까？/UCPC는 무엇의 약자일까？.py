import sys
input = sys.stdin.readline

idx = 0
target = ['U', 'C', 'P', 'C']

S = list(input().rstrip())

flag = False

for s in S:
    if s == target[idx]:
        idx += 1
    if idx == 4:
        flag = True
        break

if flag: print('I love UCPC')
else: print('I hate UCPC')
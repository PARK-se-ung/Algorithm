import sys
input = sys.stdin.readline
from collections import deque
v, p = map(int, input().split(' '))
story = [0 for _ in range(v + 1)]

truth = list(map(int, input().split(' ')))
if len(truth) > 0:
    for t in truth[1:]:
        story[t] = 1

queue = deque()

for _ in range(p):
    temp = list(map(int, input().split(' ')))
    t = temp[0]
    for i in range(1, t + 1):
        if story[temp[i]] == 1:
            for j in temp[1:]:
                story[j] = 1
            break
    if i == t and story[temp[i]] == 0:
        queue.append(temp)

N = len(queue)
for _ in range(N ** 2):
    if not queue:
        break
    li = queue.popleft()
    s = li[0]
    for i in range(1, s + 1):
        if story[li[i]] == 1:
            for j in li[1:]:
                story[j] = 1
            break
    if i == s and story[li[i]] == 0:
        queue.append(li)

print(len(queue))
import sys
input = sys.stdin.readline

n = int(input())

seq = list(map(int, input().split(' ')))
idx = [-1] * n
parent = [-1] * n

def binary_search(x):
    left, right = 0, len(sub) - 1
    while left <= right:
        mid = (left + right) // 2
        if x > seq[sub[mid]]:
            left = mid + 1
        else:
            right = mid - 1
    return left

sub = []
for i in range(n):
    pos = binary_search(seq[i])
    if len(sub) == pos:
        sub.append(i)
    else:
        sub[pos] = i
    
    idx[i] = pos
    if pos > 0:
        parent[i] = sub[pos - 1]

lis = []
index = sub[-1]
while index != -1:
    lis.append(seq[index])
    index = parent[index]

lis.reverse()

print(len(sub))
print(' '.join(map(str, lis)))
import sys
input = sys.stdin.readline

n = int(input())
arr = []
idx = dict()
for i in range(n):
    k = int(input())
    arr.append(k)
    idx[k] = i

swapped = [False] * n

for i in range(n):
    if not swapped[i] and arr[i] != 1:
        target_idx = idx[arr[i] - 1]
        if target_idx > i and not swapped[target_idx]:
            idx[arr[i]], idx[arr[target_idx]] = target_idx, i
            arr[i], arr[target_idx] = arr[target_idx], arr[i]
            swapped[i] = swapped[target_idx] = True

print('\n'.join(map(str, arr)))
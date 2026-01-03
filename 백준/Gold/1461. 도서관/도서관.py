import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
if m >= n:
    print(max(abs(x) for x in arr)) if arr[-1] * arr[0] > 0 else print(min(2 * abs(arr[0]) + arr[-1], abs(arr[0]) + 2 * arr[-1]))
    sys.exit(0)

result = 0

def func(start, end):
    return 2 * (sum(start[i] for i in range(len(start) - 1, -1, -m)) 
    + sum(end[i] for i in range(len(end) - m - 1, -1, -m))) + end[-1]

if arr[0] * arr[-1] > 0:
    arr.sort(key = lambda x : abs(x))
    step = arr[-1] + 2 * sum(arr[i] for i in range(n - m - 1, -1, -m))
    result = abs(step)
else:
    positive, negative = [], []
    for elem in arr:
        if elem > 0: positive.append(elem)
        else: negative.append(abs(elem))
    negative.sort()
    result = func(positive, negative) if positive[-1] < negative[-1] else func(negative, positive)

print(result)
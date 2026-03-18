import sys
input = sys.stdin.readline

n, k = map(int, input().split())
height = list(map(int, input().split()))
diff = [abs(height[i + 1] - height[i]) for i in range(n - 1)]

def func(x):
    tired = 0
    prev = False
    for i in range(n - 1):
        if diff[i] > x:
            tired += 1
            if not prev:
                tired += 1
                prev = True
        else:
            prev = False
    return tired

left, right = 0, 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if func(mid) > k:
        left = mid + 1
    else:
        right = mid - 1

print(left)
import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
between = list(map(int, input().split()))
confuse = list(map(int, input().split()))

dp = [confuse[0]] * n

def func(i):
    upper = time[i] - between[i]
    left, right = 0, i - 1
    while left <= right:
        mid = (left + right) // 2
        if time[mid] < upper:
            left = mid + 1
        else:
            right = mid - 1
    return right

for i in range(1, n):
    idx = func(i)
    bias = 0 if idx == -1 else dp[idx]
    dp[i] = max(dp[i - 1], bias + confuse[i])

print(dp[n - 1])
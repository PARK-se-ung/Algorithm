import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = list(map(int, input().split()))
target = arr[l - 1 : r]
flag = 1
if (l > 1 and min(target) < max(arr[:l - 1])) or (r < n and max(target) > min(arr[r:])):
    flag = 0

print(flag)

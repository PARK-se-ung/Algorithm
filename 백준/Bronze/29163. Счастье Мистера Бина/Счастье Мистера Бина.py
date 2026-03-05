import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
odd, even = 0, 0
for i in range(n):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print("Happy") if even > odd else print("Sad")
import sys
input = sys.stdin.readline


result = ["Gnomes:"]
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if arr[0] < arr[1] < arr[2] or arr[0] > arr[1] > arr[2]:
        result.append("Ordered")
    else:
        result.append("Unordered")

print('\n'.join(result))
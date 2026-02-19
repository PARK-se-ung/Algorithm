import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(n):
    temp = []
    while arr[i] > 0:
        temp.append(result.pop())
        arr[i] -= 1
    result.append(i + 1)
    while temp:
        result.append(temp.pop())
    
print(' '.join(map(str, result)))
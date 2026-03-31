import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)
    
def lcm(x, y):
    return (x * y) // gcd(x, y)

result = float('inf')
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            result = min(result, lcm(lcm(arr[i], arr[j]), arr[k]))
print(result)
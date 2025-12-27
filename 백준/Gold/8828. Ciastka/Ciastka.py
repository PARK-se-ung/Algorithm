import sys
input = sys.stdin.readline

def my_input():
    current = input()
    while current.strip() == "":
        current = input()
    return int(current)

for _ in range(my_input()):
    n = my_input()
    arr = []
    while len(arr) < n:
        line = input().strip()
        if not line:
            continue
        arr.extend(map(int, line.split()))

    if n % 2 == 1: 
        arr.append(0)
        n += 1
    arr.sort(key = lambda x : -x)

    diff = [arr[i] - arr[i + 1] for i in range(n - 1)]
    diff.append(0)
    current = sum(diff[1::2]) + arr[-1]
    start = min(sum(diff[::2]), current)

    for i in range(0, n - 1, 2):
        current += diff[i] - diff[i + 1]
        start = min(start, current)
    
    print(start)
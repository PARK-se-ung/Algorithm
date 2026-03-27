import sys
input = sys.stdin.readline


n = int(input())
arr = [i % 6 for i in range(n)]
ex_total = sum(arr) * 9

candidate = set(i for i in range(n))

while len(candidate) > 1:
    print('?', end = ' ')
    print(' '.join(map(str, arr)))
    sys.stdout.flush()
    total = int(input())
    if total == -1: sys.exit(0)

    res = total - ex_total
    idx = 0
    new_candidate = set()
    for i in range(n):
        if arr[i] == res and i in candidate:
            arr[i] = idx
            idx = (idx + 1) % 6
            new_candidate.add(i)
        else:
            arr[i] = 0
    candidate = new_candidate
    ex_total = sum(arr) * 9

for i in range(n):
    if i in candidate:
        print(f"! {i + 1}")
        sys.stdout.flush()
        break
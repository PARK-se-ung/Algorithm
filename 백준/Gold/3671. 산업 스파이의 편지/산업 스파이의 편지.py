import sys
input = sys.stdin.readline

def permutation(arr):
    result = set()

    def backtrack(start, current):
        if start > 0:
            result.add(current)
        
        if start == len(arr): return

        prev = set()
        for i in range(start, len(arr)):
            if arr[i] in prev: continue

            prev.add(arr[i])

            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1, current * 10 + arr[start])
            arr[start], arr[i] = arr[i], arr[start]

    backtrack(0, 0)

    return result

size = 1 + int(10 ** 7)

def eratos(size):
    prime = bytearray([1] * size)
    prime[0] = prime[1] = 0

    for i in range(2, int(size ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, size, i):
                prime[j] = 0

    return prime

prime = eratos(size)

for _ in range(int(input())):
    arr = list(map(int, list(input().rstrip())))
    candidate = permutation(arr)

    print(sum(1 for c in candidate if prime[c]))

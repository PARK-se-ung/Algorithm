import sys
input = sys.stdin.readline

def distribute(n, A, B, C):
    for elem in (A, B, C):
        if elem[0] > n - elem[1]:
            return 0
    return 1

n = int(input())
A, B, C = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))

if not distribute(n, A, B, C): print(0)
else:
    print(1)
    result = [(0, 0) for _ in range(3)]

    # A
    if A[0] <= C[1]: 
        result[0] = (0, A[0])
        C[1] -= A[0]
    else: 
        result[0] = (A[0] - C[1], C[1])
        B[1] -= A[0] - C[1]
        C[1] = 0
        
    # B
    result[1] = (B[0] - C[1], C[1])
    A[1] -= B[0] - C[1]

    # C
    result[2] = (A[1], B[1])

    for elem in result:
        print(' '.join(map(str, elem)))
import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())

if x == y == 0:
    print(0)
    sys.exit(0)

A, B, C, D = (0, 0), (0, n), (n, n), (n, 0)
result = []

cx, cy = 0, 0

while x > 0 and y > 0:
    bias = min(n - 1, x, y)
    A = (A[0] + bias, A[1] + bias)
    B = (B[0] + bias, B[1] + bias)
    C = (C[0] + bias, C[1] + bias)
    D = (D[0] + bias, D[1] + bias)
    result.append(("A", A[0], A[1]))
    result.append(("B", B[0], B[1]))
    result.append(("D", D[0], D[1]))
    result.append(("C", C[0], C[1]))
    x -= bias
    y -= bias

while x > 0:
    bias = min(n - 1, x)
    A = (A[0] + bias, A[1])
    B = (B[0] + bias, B[1])
    C = (C[0] + bias, C[1])
    D = (D[0] + bias, D[1])
    result.append(("A", A[0], A[1] + bias))
    result.append(("B", B[0], B[1]))
    result.append(("D", D[0], D[1] + bias))
    result.append(("C", C[0], C[1]))
    result.append(("A", B[0] + n // 2, B[1] - n // 2))
    result.append(("D", D[0], D[1]))
    result.append(("A", A[0], A[1]))
    x -= bias

while y > 0:
    bias = min(n - 1, y)
    A = (A[0], A[1] + bias)
    B = (B[0], B[1] + bias)
    C = (C[0], C[1] + bias)
    D = (D[0], D[1] + bias)
    result.append(("A", A[0] + bias, A[1]))
    result.append(("B", B[0] + bias, B[1]))
    result.append(("D", D[0], D[1]))
    result.append(("C", C[0], C[1]))
    result.append(("A", D[0] - n // 2, D[1] + n // 2))
    result.append(("B", B[0], B[1]))
    result.append(("A", A[0], A[1]))
    y -= bias

print(len(result))
for i in range(len(result)):
    print(' '.join(map(str, result[i])))
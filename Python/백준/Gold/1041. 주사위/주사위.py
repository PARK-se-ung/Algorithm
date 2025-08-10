import sys
input = sys.stdin.readline

n = int(input())
a, b, c, d, e, f = map(int, input().split(' '))
if n == 1:
    print(a + b + c + d + e + f - max(a, b, c, d, e, f))
else:
    temp1 = min(b + c, c + e, e + d, d + b)
    temp2 = min(a, f)
    face_3 = temp1 + temp2
    face_2 = min(temp1, temp2 + min(b, c, d, e))
    face_1 = min(a, b, c, d, e, f)
    print(4 * face_3 + (8 * n - 12) * face_2 + (5 * n * n - 16 * n + 12) * face_1)
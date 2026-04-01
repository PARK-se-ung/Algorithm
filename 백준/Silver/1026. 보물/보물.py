import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
cnt = sum(1 for elem in A if elem == 0)
if cnt == n: print(0)
else: print(sum(A[i + cnt] * B[n - 1 - cnt - i] for i in range(n - cnt)))
import sys
input = sys.stdin.readline

def func(S):
    h, m = map(int, S.split(':'))
    return 60 * h + m

x, y = func(input().rstrip()), func(input().rstrip())
print("YES") if x < y else print("NO")
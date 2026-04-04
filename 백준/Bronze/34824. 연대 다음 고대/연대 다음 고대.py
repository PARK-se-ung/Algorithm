import sys
input = sys.stdin.readline

flag = False
for _ in range(int(input())):
    n = input().rstrip()
    if n == "korea":
        flag = True
    elif n == "yonsei":
        if flag: print("Yonsei Lost...")
        else: print("Yonsei Won!")
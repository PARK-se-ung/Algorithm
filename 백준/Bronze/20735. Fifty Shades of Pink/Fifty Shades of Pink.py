import sys
input = sys.stdin.readline

result = 0
for _ in range(int(input())):
    S = input().rstrip().upper()
    for i in range(len(S) - 3):
        if S[i : i + 4] in {"PINK", "ROSE"}:
            result += 1
            break
print(result) if result > 0 else print("I must watch Star Wars with my daughter")

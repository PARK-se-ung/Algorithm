import sys
input = sys.stdin.readline


def check(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        elif len(stack) == 1:
            if stack[-1] == '0':
                if s[i] == '0': return "NO"
                stack = []
            else:
                if s[i] == '1': return "NO"
                stack.append(s[i])
        elif len(stack) == 2:
            if s[i] == '1': return "NO"
            stack.append(s[i])
        elif len(stack) == 3:
            if s[i] == '1': stack.append(s[i])
        elif len(stack) == 4:
            if s[i] == '1': 
                if check(s[i:]) == "YES": return "YES"
            else:
                stack = ['0']

    if not stack or stack == ['1', '0', '0', '1']:
        return "YES"
    return "NO"
        
for _ in range(int(input())):
    print(check(input().rstrip()))

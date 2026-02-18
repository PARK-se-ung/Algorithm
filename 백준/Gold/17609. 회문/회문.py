import sys
input = sys.stdin.readline

def pal(str, flag):
    l = len(str)
    result = 0
    for i in range(l // 2):
        if str[i] != str[l - i - 1]:
            result = 1
            if not flag:
                left, right = pal(str[i:l - i - 1], True), pal(str[i + 1: l - i], True)
                result += min(left, right)
            break
    return result

for _ in range(int(input())):
    print(pal(input().rstrip(), False))
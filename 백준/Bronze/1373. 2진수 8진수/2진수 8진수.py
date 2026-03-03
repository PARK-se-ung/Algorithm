import sys
input = sys.stdin.readline

def oct(arr):
    result = 0
    bias = 1
    for elem in arr:
        if elem == '1':
            result += bias 
        bias *= 2

    return result


binary = list(input().rstrip())[::-1]
result = []
idx = 0
while idx < len(binary):
    result.append(oct(binary[idx: min(idx + 3, len(binary))]))
    idx += 3

print(''.join(map(str, result[::-1])))
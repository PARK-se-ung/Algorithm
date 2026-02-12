import sys
input = sys.stdin.readline

order = {
    0:'z',
    1:'o',
    2:'tw',
    3:'th',
    4:'fo',
    5:'fi',
    6:'si',
    7:'se',
    8:'e',
    9:'n'
    }

def convert(x):
    result = str()
    while x > 0:
        result = order[x % 10] + result
        x //= 10
    return result

m, n = map(int, input().split())
arr = list(range(m, n + 1))
arr.sort(key = convert)

for i in range(0, n - m + 1, 10):
    print(' '.join(map(str, arr[i: min(i + 10, n - m + 1)])))

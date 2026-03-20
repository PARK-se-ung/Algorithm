import sys
input = sys.stdin.readline

while True:
    try:
        arr = list(input().rstrip())
        if not arr: break
        for i in range(len(arr)):
            if arr[i] == 'i': arr[i] = 'e'
            elif arr[i] == 'e': arr[i] = 'i'
            elif arr[i] == 'I': arr[i] = 'E'
            elif arr[i] == 'E': arr[i] = 'I'
        print(''.join(arr))
    except EOFError:
        break

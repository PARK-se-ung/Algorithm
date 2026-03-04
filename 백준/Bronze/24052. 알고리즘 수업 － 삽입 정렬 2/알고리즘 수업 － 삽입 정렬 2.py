import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def insertion(arr, n, k):
    
    flag = 0

    for i in range(1, n):
        loc = i - 1
        new_item = arr[i]

        while 0 <= loc and new_item < arr[loc]:
            arr[loc + 1] = arr[loc]
            flag += 1
            if flag == k:
                return arr
            loc -= 1
        
        if loc + 1 != i:
            arr[loc + 1] = new_item
            flag += 1

    if flag == k:
        return arr

    return -1

try:
    print(' '.join(map(str, insertion(arr, n, k))))
except:
    print(-1)
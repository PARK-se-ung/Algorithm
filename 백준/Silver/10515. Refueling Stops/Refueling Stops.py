import sys
input = sys.stdin.readline

for i in range(int(input())):
    arr = list(map(int, input().split()))
    goal, k, s = arr[0], arr[1], arr[2]
    arr = arr[3:]

    result = []

    # 현재 도달가능한 최대 거리 k
    prev, current = k, k
    for j in range(s):
        if arr[j] > current:
            break
        
        # if arr[j] <= current:
        if arr[j] <= prev:
            if not result:
                result.append(arr[j])
            else:
                result[-1] = arr[j]
        else: # arr[j] > prev
            if result and result[-1] + k >= goal:
                break
            prev = current
            result.append(arr[j])

        current = k + arr[j]

    
    if current >= goal:
        print(f"Case #{i + 1}: {' '.join(map(str, result))}")
    else:
        print(f"Case #{i + 1}: out of petrol")

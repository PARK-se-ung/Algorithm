import sys
input = sys.stdin.readline

result = 0

for i in {'A', 'B'}:
    for j in range(1, 10):
        print(f"? {i} {j}", flush = True)

        response = int(input())
        if response == 1: 
            result += j
            break

print(f"! {result}")
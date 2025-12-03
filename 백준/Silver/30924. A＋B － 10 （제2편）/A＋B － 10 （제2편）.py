import sys, random
input = sys.stdin.readline

def interact(symbol):
    arr = [i for i in range(1, 10 ** 4 + 1)]
    random.shuffle(arr)
    for j in arr:
        print(f"? {symbol} {j}", flush = True)

        if int(input()) == 1: 
            return j

    return None

a, b = interact('A'), interact('B')

print(f"! {a + b}")
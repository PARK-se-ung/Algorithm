import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
shuttle, walk = False, False
if a + b <= d: shuttle = True
if c <= d: walk = True
if shuttle:
    if walk:
        print("~.~")
    else:
        print("Shuttle")
else:
    if walk:
        print("Walk")
    else:
        print("T.T")
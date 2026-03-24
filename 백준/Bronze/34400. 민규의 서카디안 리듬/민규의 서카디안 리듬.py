import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print("ONLINE") if int(input()) % 25 < 17 else print("OFFLINE")
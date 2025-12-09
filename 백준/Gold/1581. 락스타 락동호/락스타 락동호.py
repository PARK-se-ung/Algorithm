import sys
input = sys.stdin.readline

ff, fs, sf, ss = map(int, input().split())

if ff == 0:
    if fs == 0:
        print(ss if sf == 0 else ss + 1)
    else:
        if fs > sf:
            print(ss + 2 * sf + 1)
        else:
            print(ss + 2 * fs)
else:
    if fs == 0:
        print(ff)
    else:
        if fs > sf:
            print(ff + ss + 2 * sf + 1)
        else:
            print(ff + ss + 2 * fs)
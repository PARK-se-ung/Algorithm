import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == 'end': break

    if s == 'animal': print('Panthera tigris')
    elif s == 'flower': print('Forsythia koreana')
    elif s == 'tree': print('Pinus densiflora')
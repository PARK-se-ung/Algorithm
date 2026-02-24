import sys

def convert(x):
    layer, scale = 1, 0
    while layer < x:
        scale += 1
        layer += 6 * scale

    start = [scale, 0]
    bias = [[0, -1], [-1, 0], [-1, 1], [0, 1], [1, 0], [1, -1]]
    for i in range(layer - x):
        start[0] += bias[i // scale][0]
        start[1] += bias[i // scale][1]
    
    return ' '.join(map(str, start))

while True:
    try:
        print(convert(int(input())))
    except:
        sys.exit(0)
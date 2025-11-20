import sys
input = sys.stdin.readline 


n = int(input())

# 벡터 외적
def cross_product(u, v):
    return (
        u[1] * v[2] - u[2] * v[1], 
        u[2] * v[0] - u[0] * v[2], 
        u[0] * v[1] - u[1] * v[0]
    )

def func(x1, y1, x2, y2, x3, y3, x4, y4):
    # 기울기 동일?
    if (x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1) == 0:
        # 한 직선?
        if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) == 0:
            return ['LINE']
        else:
            return ['NONE']

    # 교점 찾기
    line = cross_product(
                cross_product((x1, y1, 1), (x2, y2, 1)), 
                cross_product((x3, y3, 1), (x4, y4, 1))
            )
    return [
            'POINT', 
            str(f'{round(line[0] / line[2], 2):.2f}'),
            str(f'{round(line[1] / line[2], 2):.2f}')
        ]


for _ in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    print(' '.join(func(x1, y1, x2, y2, x3, y3, x4, y4)))
#1064

import math

def slopee(x1, y1, x2, y2):
    if (y2-y1) == 0 or (x2-x1) == 0:
        return 0
    else:
        slope = (y2 - y1) / (x2 - x1)
        return slope

def sidelen(x1, y1, x2, y2):
    len = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return len

a = []
a= list(map(int, input().split()))

slope = [slopee(a[2], a[3], a[0], a[1]), slopee(a[4], a[5], a[0], a[1]), 
        slopee(a[4],a[5],a[2],a[3])]

if  slope[0] == slope[1] and slope[0] == slope[2]:
    print(-1)
    exit()

side = [sidelen(a[0], a[1], a[2], a[3]), sidelen(a[0], a[1], a[4], a[5]), 
        sidelen(a[2], a[3], a[4], a[5])]

side = sorted(side, reverse = True)
largest = side[0] * 2 + side[1] * 2
smallest = side[1] * 2 + side[2] * 2
print(largest - smallest)
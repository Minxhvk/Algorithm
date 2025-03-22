import sys

def get():
    return sys.stdin.readline().rstrip()


N, M = map(int, get().split())
arr_A = list(map(int, get().split()))
arr_B = list(map(int, get().split()))
new_arr = []

point_a = 0
point_b = 0

while len(new_arr) < N+M:
    
    if point_a >= N:
        new_arr.append(arr_B[point_b])
        point_b += 1
    elif point_b >= M:
        new_arr.append(arr_A[point_a])
        point_a += 1
    else:
        if arr_A[point_a] <= arr_B[point_b]:
            new_arr.append(arr_A[point_a])
            point_a += 1
        else:
            new_arr.append(arr_B[point_b])
            point_b += 1

print(" ".join(str(x) for x in new_arr))
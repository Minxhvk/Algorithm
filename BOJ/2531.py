import sys

def get():
    return sys.stdin.readline().rstrip()

N, D, K, C = map(int, get().split())

arr = list(int(get()) for _ in range(N))

# 시간 초과
# is_in_table = C in arr
# max_size = 0
# for i in range(N):

#     temp_list = []
#     temp_list.append(arr[i])

#     for j in range(1, K+1):
#         temp_list.append(arr[j%N])

#     temp_set = set(temp_list)
#     temp_len = len(temp_set)

#     # temp_set에 없고, Table에 있을 경우
#     if is_in_table and C not in temp_set:
#         temp_len += 1
        
#     max_size = max(max_size, temp_len)

# print(max_size)

p1, p2 = 0, K-1
max_size = 0

while p1 < N:
    if p2 >= N:
        plates = arr[p2%N-1:p1+1:-1]
    else:
        plates = arr[p1:p2+1]

    temp_set = set(plates)
    temp_len = len(temp_set)
    if C not in plates:
        temp_len += 1
    
    max_size = max(max_size, temp_len)

    p1 += 1
    p2 += 1

print(max_size)


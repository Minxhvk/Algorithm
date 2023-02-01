import sys


def get():
    return sys.stdin.readline().rstrip()


n = int(get())

input_arr = list(map(int, get().split()))
result_arr = [0 for _ in range(n)]

result_arr[0] = input_arr[0]
result = input_arr[0]

for i in range(1, n):
    result_arr[i] = max(input_arr[i], result_arr[i-1] + input_arr[i])
    result = max(result, result_arr[i])

print(result)


# 처음 풀이 ( 이것도 정답이긴 함 )
# import sys


# def get():
#     return sys.stdin.readline().rstrip()


# n = int(get())

# input_arr = list(map(int, get().split()))
# result_arr = [[-1, 0] for _ in range(n)]

# result_arr[0][0] = input_arr[0]
# result_arr[0][1] = input_arr[0]
# result = input_arr[0]

# for i in range(1, n):
#     if input_arr[i] < 0:
#         if (result_arr[i-1][1] + input_arr[i]) > 0:
#             result_arr[i][1] = result_arr[i-1][1] + input_arr[i]

#     if result_arr[i-1][0] > 0:  # 연속된 수 들이 양수일 경우
#         result_arr[i][0] = result_arr[i-1][0] + input_arr[i]
#         result_arr[i][1] = result_arr[i-1][1] + input_arr[i]
#     else:
#         result_arr[i][0] = input_arr[i]
#         result_arr[i][1] = result_arr[i-1][1] + input_arr[i]
#     result = max(result, result_arr[i][0], result_arr[i][1])

# print(result)

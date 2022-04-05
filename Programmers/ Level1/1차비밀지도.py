# 나의 풀이
def solution(n, arr1, arr2):
    answer = []
    new_arr1 = [[0 for _ in range(n)] for _ in range(n)]
    new_arr2 = [[0 for _ in range(n)] for _ in range(n)]
    sub_str = ''
    for i in range(n):
        new_arr1[i] = format(arr1[i], 'b').zfill(n)
        new_arr2[i] = format(arr2[i], 'b').zfill(n)

    for i in range(n):
        sub_str = ''
        for j in range(n):
            if new_arr1[i][j] == '1' or new_arr2[i][j] == '1':
                sub_str += '#'
            elif new_arr1[i][j] == '0' and new_arr2[i][j] == '0':
                sub_str += ' '
        answer.append(sub_str)

    return answer

# 다른사람 풀이


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer

# 수정 풀이


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # bin() >> 0b~ 나오므로 [2:]
        # zfill >> 자릿수 맞추기
        new_arr = bin(arr1[i] | arr2[i])[2:].zfill(n)
        sub_str = ''
        for j in new_arr:
            if j == '1':
                sub_str += '#'
            else:
                sub_str += ' '
        answer.append(sub_str)

    return answer

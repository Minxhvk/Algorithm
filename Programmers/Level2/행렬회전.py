def solution(rows, columns, queries):
    answer = []
    nums = [[col+columns*row for col in range(1, columns + 1)]
            for row in range(rows)]
    for y1, x1, y2, x2 in queries:
        y1 -= 1
        x1 -= 1
        y2 -= 1
        x2 -= 1
        tmp = nums[y1][x1]
        min_value = tmp

        for i in range(y1, y2):
            value = nums[i+1][x1]
            nums[i][x1] = value
            min_value = min(min_value, value)

        for i in range(x1, x2):
            value = nums[y2][i+1]
            nums[y2][i] = value
            min_value = min(min_value, value)

        for i in range(y2, y1, -1):
            value = nums[i-1][x2]
            nums[i][x2] = value
            min_value = min(min_value, value)

        for i in range(x2, x1, -1):
            value = nums[y1][i-1]
            nums[y1][i] = value
            min_value = min(min_value, value)

        nums[y1][x1 + 1] = tmp
        answer.append(min_value)

    return answer

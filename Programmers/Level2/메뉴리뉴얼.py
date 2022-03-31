import collections
from itertools import combinations
import itertools

# 내 풀이


def solution(orders, course):
    answer = []
    dict = collections.defaultdict(int)
    temp = ''
    max_value = 0

    for curr_idx in range(len(orders)):
        for next_idx in range(curr_idx+1, len(orders)):
            for curr_char in orders[curr_idx]:
                for next_char in orders[next_idx]:
                    if curr_char == next_char:
                        temp = temp + curr_char
            if len(temp) >= 2:
                for i in range(2, len(temp) + 1):
                    for temp_elemnet in list(combinations(temp, i)):
                        dict[''.join(sorted(temp_elemnet))] += 1

            temp = ''

    for i in course:
        for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True):
            if i == len(key) and value >= max_value:
                answer.append(key)
                max_value = value
        max_value = 0

    return sorted(answer)

# 다른 사람 풀이


def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(
                sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v >
                   1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(result)]

from collections import defaultdict


def solution(genres, plays):
    answer = []
    tot = []
    dict = defaultdict(int)

    # 합계 구하기
    for i, j in enumerate(zip(genres, plays)):
        tot.append([i, j])
        dict[j[0]] += j[1]

    # 합계에 따라 dict 정렬
    dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

    # 많이 들은 순 정렬
    tot.sort(key=lambda x: (x[1][0], x[1][1]), reverse=True)

    for i, _ in dict:
        cnt = 0
        for j in range(len(tot)):
            if i == tot[j][1][0] and cnt < 2:
                answer.append(tot[j][0])
                tot[j][0] = ''
                cnt += 1

    return answer

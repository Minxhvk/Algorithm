import collections


def solution(id_list, report, k):
    answer = []
    report = list(set(report))  # 중복 제거
    reported_list = collections.defaultdict(list)
    count_report = collections.defaultdict(int)
    for i in report:
        # {신고당한사람 = [신고한사람1, 신고한사람2]}
        reported_list[i.split()[1]].append(i.split()[0])

    for i in reported_list:
        if len(reported_list[i]) >= k:
            for j in reported_list[i]:
                count_report[j] += 1  # 메일 받을 횟수

    for i in id_list:
        answer.append(count_report[i])
    return answer

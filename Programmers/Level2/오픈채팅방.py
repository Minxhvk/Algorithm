from collections import defaultdict


def solution(record):
    name_dict = defaultdict(int)
    answer = []

    for i in record[::-1]:
        record_str = i.split()
        if record_str[0] == "Leave":
            continue
        user_id = record_str[1]
        user_name = record_str[2]
        if name_dict[user_id] == 0:
            name_dict[user_id] = user_name

    for i in record:
        record_str = i.split()
        user_do = record_str[0]
        user_id = record_str[1]

        if user_do == "Enter":
            answer.append(name_dict[user_id] + "님이 들어왔습니다.")
        elif user_do == "Leave":
            answer.append(name_dict[user_id] + "님이 나갔습니다.")

    return answer


solution(["Enter uid1234 Muzi"])

import datetime

# 참고 답


def solution(a, b):
    # 1월1일이 금요일이므로 7로 나눴을 때 인덱스 1이 금요일로 나오게 배열을 설정
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 달의 날짜만큼 배열로 저장

    # mon배열의 (a-1)월까지 더한수에 <- 3월이면 2월까지의 날짜 다 더한수
    return day[(sum(mon[:a-1]) + b) % 7]
    # 구하고자하는 b날짜를 더하고 7로 나눈 나머지의 인덱스에 해당하는 수 반환


def getDayName(a, b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()  # list로 저장됨
    # weekday : 요일을 인덱스로 반환
    return t[datetime.datetime(2016, a, b).weekday()]

import sys


def get():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    n = int(get())
    arr_day = []
    arr_pay = []

    for _ in range(n):
        day, pay = map(int, get().split())

        arr_day.append(day)
        arr_pay.append(pay)

    dp = [0 for i in range(n+1)]

    for i in range(n-1, -1, -1):
        if arr_day[i] + i <= n:
            dp[i] = max(arr_pay[i] + dp[i + arr_day[i]], dp[i+1])
        else:
            dp[i] = dp[i+1]

    print(dp[0])

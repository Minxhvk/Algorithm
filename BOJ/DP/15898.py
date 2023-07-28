import sys

def get():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":

    cnt = int(get())

    arr = list(int(get()) for _ in range(cnt))

    dp = [[0 for _ in range(4)] for _ in range(10001)]


    dp[1][0] = 1
    dp[2][0] = 1
    dp[2][1] = 1
    dp[3][0] = 1
    dp[3][1] = 1
    dp[3][2] = 1

    for i in range(4, 10001):
        dp[i][0] = 1 # 1로 이루는 경우는 오직 1개
        dp[i][1] = 1 + dp[i - 2][1]
        dp[i][2] = dp[i - 3][0] + dp[i - 3][1] + dp[i - 3][2]

    for i in arr:
        print(dp[i][0] + dp[i][1] + dp[i][2])


"""
1
1

2
1 1 / 2

3
1 1 1 / 2 1 / 3

4
1 1 1 1 / 2 1 1 / 2 2 / 3 1

5
1 1 1 1 1 / 2 1 1 1 / 2 2 1 / 3 1 1 / 3 2 

"""


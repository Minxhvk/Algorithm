import sys


def NQueen(k):
    global result

    if k == N:
        result += 1
        return

    for idx in range(N):
        # 우 대각 x-y 의 값이 음수가 될 수 있으므로 +N
        # 어차피 x-y값이 똑같기 때문에 +N을 해도 고정 값인건 똑같다.
        if not isused_1[idx] and not isused_2[k+idx] and not isused_3[k-idx+N]:
            isused_1[idx] = True
            isused_2[k+idx] = True
            isused_3[k-idx+N] = True

            NQueen(k+1)

            isused_1[idx] = False
            isused_2[k + idx] = False
            isused_3[k - idx + N] = False


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    isused_1 = [False for _ in range(40)]
    isused_2 = [False for _ in range(40)]  # 좌측 하단 -> 우측 상단 판단 : x + y 의 값이 같은지
    isused_3 = [False for _ in range(40)]  # 우측 하단 -> 좌측 상단 판단 : x - y 의 값이 같은지

    result = 0

    NQueen(0)
    print(result)

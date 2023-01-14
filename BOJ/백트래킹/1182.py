import sys


def get():
    return sys.stdin.readline().rstrip().split()


def get_sum(idx, tot):
    global result

    if idx == size:
        if tot == target:
            result += 1

        return

    get_sum(idx+1, tot)  # 원소를 안 더한 상태로 진행
    get_sum(idx+1, tot + arr[idx])  # 원소를 더한 상태로 진행


if __name__ == "__main__":
    size, target = map(int, get())
    arr = list(map(int, get()))

    result = 0

    get_sum(0, 0)

    print(result)

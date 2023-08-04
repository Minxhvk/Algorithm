import bisect
import sys


def get():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N, C = map(int, get().split())

    arr = sorted([int(get()) for _ in range(N)])

    min_diff = 1
    max_diff = max(arr) - min(arr)

    while True:
        mid = ( min_diff + max_diff ) // 2

        starter = arr[0]
        starter_idx = 0
        router_cnt = 0

        while starter_idx < len(arr):
            router_cnt += 1
            starter_idx = bisect.bisect_left(arr, arr[starter_idx] + mid)

        if router_cnt < C:
            max_diff = mid - 1
        else:
            min_diff = mid + 1

        if mid == max_diff:
            print(mid)
            break


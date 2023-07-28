import sys


def convert(arr):

    converted_str = ''

    for i in arr:
        if len(i) <= 0 : continue

        if "K" in i:
            converted_str += str(int(5 * (10**(len(i)-1))))
        else:
            converted_str += str(int(10 ** (len(i) - 1)))

    return converted_str



if __name__ == "__main__":
    """
    최대 : K가 있을 때에 M과 조합하는 쪽이 큼
    최소 : K는 단일, M은 연속될 수록 작음
    """

    target = list(sys.stdin.readline().rstrip())

    max_arr = []
    min_arr = []

    k_idx = None
    temp_str = ""

    # 최대
    for i in range(len(target)):
        if "K" not in target[i:]:
            for _ in range(i, len(target)):
                max_arr.append("M")
            break

        if target[i] == "K":
            if k_idx is None:
                max_arr.append("".join(target[:i + 1]))
            else:
                max_arr.append("".join(target[k_idx + 1:i + 1]))
            k_idx = i

    # 최소
    for i in range(len(target)):
        if target[i] == "K":
            if len(temp_str) > 0:
                min_arr.append(temp_str)

            min_arr.append(target[i])
            temp_str = ""
        else:
            temp_str += target[i]

    if len(temp_str) > 0: min_arr.append(temp_str)

    print(convert(max_arr))
    print(convert(min_arr))
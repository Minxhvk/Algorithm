import sys


def get():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(get())

    switch_list = list(map(int, get().split()))

    student_num = int(get())

    st_num_list = [list(map(int, get().split())) for _ in range( student_num)]

    for i in st_num_list:
        s = i[0]
        num = i[1]

        if s == 1:
            for j in range(1, N+1):
                if j % num == 0:
                    if switch_list[j-1] == 1:
                        switch_list[j-1] = 0
                    else:
                        switch_list[j-1] = 1

        else:
            num -= 1
            if switch_list[num] == 1:
                switch_list[num] = 0
            else:
                switch_list[num] = 1

            j = 1
            while True:
                if num + j >= N or num - j < 0: break

                if switch_list[num+j] != switch_list[num-j]:
                    break

                if switch_list[num+j] == 1:
                    switch_list[num+j] = 0
                else:
                    switch_list[num+j] = 1

                if switch_list[num-j] == 1:
                    switch_list[num-j] = 0
                else:
                    switch_list[num-j] = 1

                j += 1

    for i in range(N):
        print(switch_list[i], end=" ")
        if (i+1) % 20 == 0 and i+1 != N:
            print()
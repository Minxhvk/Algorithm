
import sys


def get():
    return sys.stdin.readline().rstrip()


input_str = ''

dict = {
    '}': '{',
    ')': '(',
    ']': '[',
}

while True:
    input_str = get()
    if input_str == '.':
        break

    stack = []

    flag = True

    for i in input_str:
        if i in dict.values():
            stack.append(i)

        elif i in dict.keys():
            if (len(stack) <= 0) or (dict[i] != stack.pop()):
                flag = False
                break

    if len(stack) == 0 and flag == True:
        print('yes')
    else:
        print('no')

import sys


def get():
    return sys.stdin.readline().rstrip()


input_str = get()

answer = 0
line = 0
stack = []

for i in range(len(input_str)):
    if input_str[i] == '(':
        stack.append(i)

    else:
        pop_idx = stack.pop()

        if pop_idx == i-1:
            answer += len(stack)

        else:
            answer += 1

print(answer)

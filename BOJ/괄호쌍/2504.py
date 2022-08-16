import sys


def get():
    return sys.stdin.readline().rstrip()


inpurt_str = get()

stack = []
answer = 0
tmp = 1

for i in range(len(inpurt_str)):
    if inpurt_str[i] == '(':
        stack.append('(')
        tmp *= 2
    elif inpurt_str[i] == '[':
        stack.append('[')
        tmp *= 3

    elif inpurt_str[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if inpurt_str[i-1] == '(':
            answer += tmp
        tmp //= 2
        stack.pop()

    else:
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if inpurt_str[i-1] == '[':
            answer += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)

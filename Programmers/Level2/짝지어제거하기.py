def solution(s):
    x = [None]
    for i in s:
        if x[-1] == i:
            x.pop()
        else:
            x.append(i)
    if len(x) == 1:
        return 1
    else:
        return 0

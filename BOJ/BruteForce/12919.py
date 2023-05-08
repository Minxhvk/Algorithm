import sys
from collections import deque

def get():
    return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    s = get()
    t = get()
    reverse_t = t[::-1]

    s_deque = deque()
    s_deque.append(s)

    can_convert = False

    while s_deque:
        target = s_deque.popleft()

        add_a = target + 'A' # 1. A 붙이기
        add_b = (target + 'B')[::-1] # 2. B 붙이기

        if add_a == t or add_b == t:
            can_convert = True
            break
        else:
            if add_a in t or add_a in reverse_t: s_deque.append(add_a)
            if add_b in t or add_b in reverse_t: s_deque.append(add_b)

    print(1 if can_convert else 0)





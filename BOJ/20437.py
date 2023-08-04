import sys
from collections import defaultdict

def get():
    return sys.stdin.readline().rstrip()

N = int(get())

arr = []

for _ in range(N):
    arr.append([get(), int(get())])

min_3 = None
max_4 = None

for cur in arr:
    cur_str = cur[0]
    cur_cnt = cur[1]

    min_3 = sys.maxsize
    max_4 = -sys.maxsize

    counter_dict = defaultdict(list)

    for char_idx in range(len(cur_str)):
        counter_dict[cur_str[char_idx]].append(char_idx)

    for values in counter_dict.values():
        for k in range(len(values)-cur_cnt+1):
            cur_len = values[k+cur_cnt-1] - values[k] + 1

            min_3 = min(min_3, cur_len)
            max_4 = max(max_4, cur_len)
        
    if min_3 == sys.maxsize or max_4 == -sys.maxsize:
        print(-1)
    else:
        print(min_3, max_4)


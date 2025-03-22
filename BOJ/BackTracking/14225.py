import sys

def get():
    return sys.stdin.readline().rstrip()

def get_sum(idx, tot):
    
    if idx == n:
        answer_set.add(tot)
        return
    
    get_sum(idx+1, tot)
    get_sum(idx+1, tot + arr[idx])


n = int(get())
arr = list(map(int, get().split()))
answer_set = set()
get_sum(0, 0)
answer = 0

while True:
    if answer not in answer_set:
        print(answer)
        break

from collections import defaultdict
import sys

def get():
    return sys.stdin.readline().rstrip()

N, K = map(int, get().split())
arr = list(map(int, get().split()))


answer = 0
one_point = 0
two_point = 1

count_dict = defaultdict(int)

count_dict[arr[one_point]] += 1
count_dict[arr[two_point]] += 1

while True:
    if two_point == len(arr) -1 : break
    if count_dict[arr[two_point + 1]] + 1 >  K:
        count_dict[arr[one_point]] -= 1
        one_point += 1
    else:
        two_point += 1
        count_dict[arr[two_point]] += 1
        
    
    answer = max(answer, two_point - one_point + 1)

print(answer)
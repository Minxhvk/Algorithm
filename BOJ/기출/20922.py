from collections import defaultdict
import sys

def get():
    return sys.stdin.readline().rstrip()

N, K = map(int, get().split())
arr = list(map(int, get().split()))


answer = 0
left = 0
right = 0

count_dict = defaultdict(int)

while left <= right and right < N:
    while count_dict[arr[right]] == K:
        count_dict[arr[left]] -= 1
        left += 1
    answer = max(answer, right-left+1)
    
    count_dict[arr[right]] += 1
    right += 1

print(answer)
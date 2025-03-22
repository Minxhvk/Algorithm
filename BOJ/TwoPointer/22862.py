import sys

def get():
    return sys.stdin.readline().rstrip()

def is_odd(x):
    return x % 2 == 1

N, K = map(int, get().split())
nums = list(map(int, get().split()))

left = 0
right = 0
temp_len = 0
result = 0
odd_cnt = 0

# left에서 odd_cnt가 K 보다 커질때 까지 돌린다.
while right < N:
    if odd_cnt <= K:
        if is_odd(nums[right]):
            odd_cnt += 1
        else:
            temp_len += 1
        right += 1  

    else:  
        while odd_cnt > K:
            if is_odd(nums[left]):
                odd_cnt -= 1
            else:
                temp_len -= 1  
            left += 1

    result = max(result, temp_len)

print(result)
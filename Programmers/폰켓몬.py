def solution(nums):
    n = len(nums)/2
    if len(set(nums)) > n:
        return n
    else:
        return len(set(nums))

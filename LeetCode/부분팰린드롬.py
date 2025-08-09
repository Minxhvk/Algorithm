def palindrom(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return len(s[left+1:right])
    
def solution(s):
    answer = 1
    
    for i in range(len(s)-1):
        answer = max(answer, palindrom(s, i, i+1), palindrom(s, i, i+2))
        
    return answer
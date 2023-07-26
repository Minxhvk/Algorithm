def solution(k, d):
    
    answer = 0
    
    for i in range(0, d+1, k):
        y = (d**2 - i**2)**(1/2) # Y 좌표의 최댓값을 구한다.
        answer += (y//k + 1) # k의 배수이므로 나누면, Y의 갯수가 나온다. 이 때, 0도 포함되어야 하니 +1 해준다
    
    
    return answer
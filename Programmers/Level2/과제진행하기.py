from collections import deque

def convert_time(s):
    h, m = map(int, s.split(":"))
    return h*60 + m
    
def solution(plans):
    answer = []
    
    plans = [ (name, convert_time(start), int(play_time)) for name, start, play_time in plans]
    plans.sort(key=lambda x: x[1])
    
    assign_queue = deque()
    left_time = 0
    
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        
        while assign_queue:
            _name, _playtime = assign_queue.pop()
            if left_time >= _playtime: # 다음 작업까지 남은 시간보다 작업해야 하는 시간이 적을 경우
                left_time -= _playtime
                answer.append(_name)
            else: # 다음 작업을 먼저 시작해야 한다.
                assign_queue.append((_name, _playtime - left_time))
                break
                
        assign_queue.append((name, playtime))
        
        if i < len(plans)-1:
            next_start = plans[i+1][1]
            left_time = next_start - start # 다음 작업까지 남은 시간
    
    while assign_queue:
        answer.append(assign_queue.pop()[0])
        
    return answer
            
from collections import Counter

def solution(str1, str2):
    answer = 0
    
    list_1 = []
    list_2 = []
    
    i = 2
    
    while i <= len(str1):
        temp_str = str1[i-2:i]
        if temp_str.isalpha(): 
            list_1.append(temp_str.upper())
        
        i += 1
        
    i = 2
    while i <= len(str2):
        temp_str = str2[i-2:i]
        if temp_str.isalpha(): 
            list_2.append(temp_str.upper())
        
        i += 1
    
    Counter1 = Counter(list_1)
    Counter2 = Counter(list_2)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
    

print(solution("aaaaa", "aaaaaaa"))
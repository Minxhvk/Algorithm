import sys
import math

def get():
    return sys.stdin.readline()

num_class = int(get())
num_student_per_class = list(map(int, get().split()))

main, sub = map(int, get().split())

answer = 0 

for i in num_student_per_class:
    answer += 1 # main
    temp_i = i - main

    if temp_i <= 0: continue
    
    elif temp_i > 0:
        answer += math.ceil(temp_i / sub)

print(answer)
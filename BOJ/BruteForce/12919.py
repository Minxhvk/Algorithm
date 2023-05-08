import sys

def read():
    return sys.stdin.readline().rstrip()

S = list(read())
T = list(read())

while True:
    if len(S) == len(T):
        if S == T: print(1)
        else: print(0)
        break
    
        


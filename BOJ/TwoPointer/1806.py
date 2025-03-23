import sys

def get():
    return sys.stdin.readline().rstrip()


n, s = map(int, get().split())
arr = list(map(int, get().split()))

pointer = 0
temp_sum = arr[0]
answer = sys.maxsize

for i in range(n):
    while pointer < n-1 and temp_sum < s:
        pointer += 1
        temp_sum += arr[pointer]
    
    if temp_sum >= s:
        answer = min(answer, pointer-i+1)

    temp_sum -= arr[i]

print(answer if answer != sys.maxsize else 0)

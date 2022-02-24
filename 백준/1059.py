
# 1059

s = int(input())

a = list(map(int, input().split()))
b = sorted(a)
x = int(input())

start_num = 0
end_num = 0
cnt = 0

for i in range(len(b)):
    if(x < b[0]):
        start_num = 1
        end_num = b[0]
        break
    if(x > b[len(b)-1]):
        break

    if(x > b[i]):
        start_num = b[i] + 1
        end_num = b[i+1]

for i in range(start_num, end_num):
    for j in range(x, end_num):
        if(i <= x and j >= x and i < j):
            cnt += 1
print(cnt)

# 1094

x = bin(int(input())) # 2진수 문자열로 들어옴
cnt = 0

for i in x:
    if i == "1":
        cnt += 1
print(cnt)
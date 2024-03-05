
# 1015

a_size = int(input())

a = list(map(int, input().split()))
b = []

for i in a:
    cnt = 0
    for j in range(a_size):
        if i > a[j]:
            cnt += 1
    # If duplication occurs
    for k in b:
        if cnt == k:
            cnt += 1
    b.append(cnt)

print(*b)
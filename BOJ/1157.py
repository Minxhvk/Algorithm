n = input().upper()
set_n = list(set(n))

cnt_list = []

for i in set_n :
    cnt = n.count(i)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(set_n[max_index])
import sys
a, b = input().split()
a = int(a)
b = int(b)
count = 0
if a < 8 or b < 8:
    sys.exit()

#array = [[0 for col in range(a) for row in range(b)]]
array = [list(map(str, input())) for _ in range(a)]
mini = []
for i in range(a - 7):
    for j in range(b - 7):
        first_W = 0
        first_B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if array[k][l] != 'W':
                        first_W += 1
                    if array[k][l] != 'B':
                        first_B += 1
                else :
                    if array[k][l] != 'B':
                        first_W += 1
                    if array[k][l] != 'W':
                        first_B += 1
        mini.append(first_W)
        mini.append(first_B)
print(min(mini))
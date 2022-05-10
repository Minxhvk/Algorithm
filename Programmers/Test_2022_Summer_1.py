
def Solution(atoms):
    cnt = 0
    day = 0

    for i, j in zip(atoms):
        if (i > 150 and j > 75):
            if(day == 0):
                cnt += 1
            day = 0
            continue
        if (day > 0):
            day -= 1
            continue

        if(i > 80 or j > 35):
            cnt += 1
            if(i <= 150 or i <= 75):
                day += 2

    return cnt

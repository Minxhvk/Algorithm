def solution(price, money, count):
    tot_price = sum([price * i for i in range(1, count+1)])

    if tot_price > money:
        return tot_price - money
    else:
        return 0

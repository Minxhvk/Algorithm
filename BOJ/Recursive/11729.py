def func(n, start, end):
    if n == 1:
        print(start, end)
        return

    func(n-1, start, 6-start-end)

    print(start, end)

    func(n-1, 6-start-end, end)


n = int(input())

print(2**n-1)

func(n, 1, 3)

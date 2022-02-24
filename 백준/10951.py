s = []

while True:
    a, b = map(int, input().split())
    if (a is None) and (b is None):
        break
    s.append(a+b)
print(s)

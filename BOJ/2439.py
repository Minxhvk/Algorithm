
n = int(input())
if n < 1 or n > 100 :
    sys.exit()

for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)
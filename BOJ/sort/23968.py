# Bubble Sort

import sys

def get():
    return sys.stdin.readline().rstrip()

def bubble_sort(arr, target):
    n = len(arr)
    cnt = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                cnt += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]

                if cnt == target:
                    return arr[j], arr[j+1]
    return -1, -1

a, k = map(int, get().split())
arr = list(map(int, get().split()))

answer1, answer2 = bubble_sort(arr, k)

if answer1 == -1:
    print(-1)
else:
    print(answer1, answer2)


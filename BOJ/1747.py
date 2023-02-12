import sys


def isPalindrome(n):
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True


def isPrimeNumber(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':

    n = int(input())

    while True:
        if isPalindrome(str(n)) and isPrimeNumber(n):
            break

        n += 1

    print(n)

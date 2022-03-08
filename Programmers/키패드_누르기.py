def solution(numbers, hand):
    answer = ''
    left, right = 10, 12

    for i in numbers:
        if i in [1, 4, 7]:
            left = i
            answer += 'L'

        elif i in [3, 6, 9]:
            right = i
            answer += 'R'

        else:
            i = 11 if i == 0 else i
            absL = abs(i-left)
            absR = abs(i-right)
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                right = i
                answer += 'R'
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                left = i
                answer += 'L'
            else:
                if hand == 'left':
                    left = i
                    answer += 'L'
                else:
                    right = i
                    answer += 'R'

    return answer

# 못풀었음 다시

def solution(numbers, hand):
    answer = ''
    left, right = int(0), int(0)

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left = i
            answer += 'L'

        elif (i % 3) == 0:
            right = i
            answer += 'R'

        else:
            if hand == 'left' and abs(i - left) == 3:
                left = i
                answer += 'L'
                continue
            elif hand == 'right' and abs(i - right) == 3:
                right = i
                answer += 'R'
                continue
            if abs(i - left) > abs(i - right):
                right = i
                answer += 'R'
            elif abs(i - left) < abs(i - right):
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

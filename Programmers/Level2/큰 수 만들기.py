# 조합 : 시간 초과
# len(number) - k 개 뽑기 : 실패

# 더 큰 숫자가 나와서 제거한 횟수이므로 k -= 1 을 해주는 것
def solution(number, k):
    answer = []

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])

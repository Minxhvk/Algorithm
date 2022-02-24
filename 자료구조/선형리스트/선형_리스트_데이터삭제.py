# 문제 3. 입력값을 이용하여 선형 리스트의 데이터를 삭제하라.
# 제한조건: 반복문, 함수 사용
# 입력 예시: 2
# 출력 예시
# >> print(languages)
# ['파이썬', 'C', 'C++', 'JAVA']

languages = ['파이썬', 'C', 'MATLAB', 'C++', 'JAVA']

def delete_data(position):
    if position < 0 or position > len(languages):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    # 코드 작성 구간
    languages[position] = None
    length = len(languages)
    for i in range(position + 1, length, 1):
        languages[i-1] = languages[i]
        languages[i] = None
    del languages[length -1]
# 실행 구문 (아래 코드를 수정하지 마시오.)
print('# 삭제 전')
print(languages)
input_data = input('삭제할 프로그래밍 언어 위치를 입력해주세요: (예시: 2)')
delete_data(int(input_data))
print('# 삭제 후')
print(languages)
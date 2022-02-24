# 문제 2. 입력값을 이용하여 선형 리스트에 데이터를 삽입하라.
# 제한조건: 반복문, 함수 사용
# 입력 예시: MATLAB, 2
# 출력 예시
# >> print(languages)
# ['파이썬', 'C', 'MATLAB', 'C++', 'JAVA']

languages = ['파이썬', 'C', 'C++', 'JAVA']

def insert_data(language, position):
    if position < 0 or position > len(languages):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    # 코드 작성 구간
    languages.append(None)
    length = len(languages)

    for i in range(length - 1, position, -1):
        languages[i] = languages[i-1]
        languages[i - 1] = None

    languages[position] = language

# 실행 구문 (아래 코드를 수정하지 마시오.)
input_data = input('삽입할 프로그래밍 언어와 삽입할 위치를 입력해주세요: (예시: MATLAB, 2)')
language, position = input_data.split()
insert_data(language, int(position))
print(languages)
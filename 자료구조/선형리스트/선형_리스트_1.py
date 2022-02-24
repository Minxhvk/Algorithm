# 문제 1. 입력값을 이용하여 선형 리스트를 생성하라.
# 제한조건: 반복문, 함수 사용
# 입력 예시: 파이썬, C, C++, JAVA
# 출력 예시
# >> print(languages)
# ['파이썬', 'C', 'C++', 'JAVA']

languages = []

def add_data(language) :
    # 코드 작성 구간
    languages.append(None)
    length = len(languages)
    languages[length - 1] = language

# 실행 구문 (아래 코드를 수정하지 마시오.)
input_data = input('좋아하는 프로그래밍 언어 입력해주세요: ')
input_data = input_data.split()
for language in input_data:
    add_data(language)
print(languages)
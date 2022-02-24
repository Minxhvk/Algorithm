# 문제 4. 입력값을 이용하여 선형 리스트 데이터 추가, 삽입, 삭제하는 코드를 작성하라.
# 입출력 예시
# 선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 1
# 추가할 데이터--> 파이썬
# ['파이썬']
# 선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 1
# 추가할 데이터--> JAVA
# ['파이썬', 'JAVA']
# 선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 2
# 삽입할 위치--> 1
# 추가할 데이터--> MATLAB
# ['파이썬', 'MATLAB', 'JAVA']
# 선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 3
# 삭제할 위치--> 1
# ['파이썬', 'JAVA']
# 선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 4
# ['파이썬', 'JAVA']

# 데이터 추가 함수
def add_data(language) :
    # 코드 작성 부분
    languages.append(None)
    length = len(languages)
    languages[length - 1] = language

# 데이터 삽입 함수
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

# 데이터 삭제 함수
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
languages = []
select = -1	# 1: 추가, 2: 삽입, 3: 삭제, 4: 종료

while select != 4:
    select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

    if select == 1 :
        data = input("추가할 데이터--> ")
        add_data(data)
        print(languages)
    elif select == 2 :
        pos = int(input("삽입할 위치--> "))
        data = input("추가할 데이터--> ")
        insert_data(data, pos)
        print(languages)
    elif select == 3 :
        pos = int(input("삭제할 위치--> "))
        delete_data(pos)
        print(languages)
    elif select == 4 :
        print(languages)
    else :
        print("1~4 중 하나를 입력하세요.")
        continue
# 과제 1. 스택함수를 이용하여 pushed 리스트에 대해서 popped 리스트 출력결과가 발생할 수 있는지 확인하라.
# (1) 입력 예시
# pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
# (1) 출력 예시: True
# (1) 설명: 다음의 순서대로 push, pop 수행할 수 있으므로 True 출력
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# (2) 입력 예시
# pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
# (2) 출력 예시: False
# (2) 설명: 1 은 2 이전에 pop 할 수 없음

class Stack:
    def __init__(self):
        self.size = 10
        self.stack = [ None for _ in range(self.size) ]
        self.top = -1

    def is_stack_full(self):
        # 코드 작성 구간
        if self.top >= self.size - 1:
          return True
        else:
          return False

    def is_stack_empty(self):
        # 코드 작성 구간
        if self.top == -1:
          return True
        else:
          return False

    def push(self, data):
        # 코드 작성 구간
        if self.is_stack_full():
          return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        # 코드 작성 구간
        if self.is_stack_empty():
          return None
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data

    def peek(self):
        # 코드 작성 구간
        if self.is_stack_empty():
          return None
        return self.stack[self.top]


    def validate_stack_sequences(self, pushed, popped):
        # 코드 작성 구간
        lenP, i, j, s = len(pushed), 0, 0, 0
        while i < lenP:
            if ~s and popped[j] == pushed[s]:
                j += 1
                s -= 1
            else:
                s += 1
                i += 1
                if i < lenP: pushed[s] = pushed[i]
        return not s


# 실행 구문 (아래 코드를 수정하지 마시오.)
test_stack = Stack()
pushed = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
popped = [[4, 5, 3, 2, 1], [4, 3, 5, 1, 2]]
for i in range(len(pushed)):
    print(test_stack.validate_stack_sequences(pushed[i], popped[i]))
# 문제 2. 스택 함수를 이용하여 과자집에 가는길과 우리집에 오는길을 출력하라.
# 입력 예시
# stoneAry = ['빨', '주', '노', '초', '파', '남', '보']
# 출력 예시
# 과자집에 가는길:  빨 --> 주 --> 노 --> 초 --> 파 --> 남 --> 보 --> 과자집
# 우리집에 오는길:  보 --> 남 --> 파 --> 초 --> 노 --> 주 --> 빨 --> 우리집

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

test_stack = Stack()
stoneAry = ['빨', '주', '노', '초', '파', '남', '보']

print("과자집에 가는길: ", end = ' ')
# 코드 작성 구간: 스택 함수 사용
for stone in stoneAry:
  test_stack.push(stone)
  print(stone, '-->', end=' ')
print('과자집')

print("우리집에 오는길: ", end = ' ')
# 코드 작성 구간: 스택 함수 사용
while True:
  stone = test_stack.pop()
  if not stone:
    break
  print(stone, '-->', end=' ')
print('우리집')

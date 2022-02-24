# 문제 4. 큐 함수를 이용하여 대기줄을 구현하라.
# 출력 예시
# 대기 줄 상태:  ['정국', '뷔', '지민', '진', '슈가', None, None, None, None, None]
# 정국 님 식당에 들어감
# 대기 줄 상태:  [None, '뷔', '지민', '진', '슈가', None, None, None, None, None]
# 뷔 님 식당에 들어감
# 대기 줄 상태:  [None, None, '지민', '진', '슈가', None, None, None, None, None]
# 지민 님 식당에 들어감
# 대기 줄 상태:  [None, None, None, '진', '슈가', None, None, None, None, None]
# 진 님 식당에 들어감
# 대기 줄 상태:  [None, None, None, None, '슈가', None, None, None, None, None]
# 슈가 님 식당에 들어감
# 대기 줄 상태:  [None, None, None, None, None, None, None, None, None, None]
# 식당 영업 종료!

class Queue:
    def __init__(self):
        self.size = 10
        self.queue = [ None for _ in range(self.size) ]
        self.front = -1
        self.rear = -1

    def is_queue_full(self):
        # 코드 작성 구간
        # 만약 큐 앞이 비어 있으면 한 칸 당기기
        if self.rear != self.size -1:
          return False
        elif self.rear == self.size - 1 and self.front == -1:
          return True
        else:
          for i in range(self.front + 1, self.size):
            self.queue[i - 1] = self.queue[i]
            self.queue[False]
          self.front -= 1
          self.rear -= 1
          return False

    def is_queue_empty(self):
        # 코드 작성 구간
        if self.front == self.rear:
          return True
        else:
          return False

    def en_queue(self, data):
        # 코드 작성 구간
        if self.is_queue_full():
          return
        self.rear += 1
        self.queue[self.rear] = data

    def de_queue(self):
        # 코드 작성 구간
        if self.is_queue_empty():
          return None
        self.front += 1
        data = self.queue[self.front]
        self.queue[self.front] = None
        return data

    def peek(self):
        # 코드 작성 구간
        if self.is_queue_empty():
          return None
        return self.queue[self.front +1]



test_queue = Queue()
test_queue.en_queue('정국')
test_queue.en_queue('뷔')
test_queue.en_queue('지민')
test_queue.en_queue('진')
test_queue.en_queue('슈가')
print("대기 줄 상태: ", test_queue.queue)

# 코드 작성 구간: 대기줄 손님들을 모두 식당에 출입시키는 과정
for i in range(test_queue.rear + 1):
  print(test_queue.de_queue(), '님 식당에 들어감')
  print('대기 줄 상태: ', test_queue.queue)

print("식당 영업 종료!")
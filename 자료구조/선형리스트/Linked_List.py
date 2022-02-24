# Node
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            # 노드의 끝에 삽입해야 하므로
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def getdataIndex(self, data):
        curn = self.head
        idx = 0
        # 처음부터 탐색하며, 검색 데이터를 만나면 index 리턴
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1

    # todo

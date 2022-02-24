class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        cur = self.head
        while cur.next == None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur.next == None:
            print(cur.data)
            cur = cur.next

    # TODO
    def get_index(self, data):
        cur = self.head
        cnt = 0
        while cur.next == None:
            if (cur.data == data):
                return cnt
            cur = cur.next
            cnt += 1
        return -1

    # def add_node:

    # def delete_node:


s1 = SinglyLinkedList(Node(1))
s1.append(Node(1))
s1.append(Node(2))
print(s1.get_index(2))

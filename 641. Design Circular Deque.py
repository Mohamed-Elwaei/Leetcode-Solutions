class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = self.tail = None
        self.limit, self.count = k, 0

    def insertFront(self, value: int) -> bool:
        if self.count == self.limit:
            return False
        self.count += 1
        node = Node(value, self.head, None)
        if self.head:
            self.head.prev = node
        else:
            self.head = self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
        self.head = node
        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.limit:
            return False
        self.count += 1
        node = Node(value, None, self.tail)
        if self.tail:
            self.tail.next = node
        else:
            self.head = self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
        self.tail = node
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False
        self.count -= 1
        tmp = self.head
        self.head = tmp.next
        self.head.prev = self.tail
        self.tail.next = self.head
        if self.count == 0:
            self.head = self.tail = None
        del tmp
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False
        self.count -= 1
        tmp = self.tail
        self.tail = tmp.prev
        self.tail.next = self.head
        self.head.prev = self.tail
        if self.count == 0:
            self.head = self.tail = None
        del tmp
        return True

    def getFront(self) -> int:
        return self.head.val if self.head else -1

    def getRear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.limit
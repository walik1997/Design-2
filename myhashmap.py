class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 10000
        self.spaces = [None] * self.size

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        if self.spaces[index] is None:
            self.spaces[index] = ListNode(key, value)
        else:
            current = self.spaces[index]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        current = self.spaces[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        current = self.spaces[index]
        if not current:
            return
        if current.key == key:
            self.spaces[index] = current.next
        else:
            prev = current
            current = current.next
            while current:
                if current.key == key:
                    prev.next = current.next
                    return
                prev, current = current, current.next
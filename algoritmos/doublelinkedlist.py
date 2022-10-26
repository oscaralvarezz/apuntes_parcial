class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return f"{self.data}"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        return "->".join([str(item) for item in self])

    def __len__(self):
        return len(tuple(iter(self)))

    def insert_at_head(self, data):
        self.insert_at_nth(0, data)

    def insert_at_tail(self, data):
        self.insert_at_nth(len(self), data)

    def insert_at_nth(self, index: int, data):
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif index == 0:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        elif index == len(self):
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            temp.previous.next = new_node
            new_node.previous = temp.previous
            new_node.next = temp
            temp.previous = new_node

    def delete_head(self):
        return self.delete_at_nth(0)

    def delete_tail(self):
        return self.delete_at_nth(len(self) - 1)

    def delete_at_nth(self, index: int):
        if not 0 <= index <= len(self) - 1:
            raise IndexError("list index out of range")
        delete_node = self.head  # default first node
        if len(self) == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.previous = None
        elif index == len(self) - 1:
            delete_node = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            delete_node = temp
            temp.next.previous = temp.previous
            temp.previous.next = temp.next
        return delete_node.data

    def delete(self, data) -> str:
        current = self.head

        while current.data != data:  # Find the position to delete
            if current.next:
                current = current.next
            else:  # We have reached the end an no value matches
                return "No data matching given value"

        if current == self.head:
            self.delete_head()

        elif current == self.tail:
            self.delete_tail()

        else:  # Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next  # 1 --> 3
            current.next.previous = current.previous  # 1 <--> 3
        return data

    def is_empty(self):
        return len(self) == 0


lista = DoublyLinkedList()
lista.insert_at_head(9)
lista.insert_at_head(10)
lista.insert_at_head(25)
lista.insert_at_head(150)
lista.delete(9)
lista.insert_at_nth(1,8)
print(lista)

from algoritmos.mergesort import mergesort
print(mergesort(lista))

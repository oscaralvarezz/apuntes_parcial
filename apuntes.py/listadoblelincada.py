class Node:
    def __init__(self, data):
        self.data = data
        self.previo = None
        self.siguiente = None

    def __str__(self):
        return f"{self.data}"


class ListaDobleLincada:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        >>> lista_lincada = ListaDobleLinc()
        >>> lista_lincada.insert_at_head('b')
        >>> lista_lincada.insert_at_head('a')
        >>> lista_lincada.insert_at_tail('c')
        >>> tupla(lista_lincada)
        ('a', 'b', 'c')
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        """
        >>> lista_lincada = ListaDobleLinc()
        >>> lista_lincada.insert_at_tail('a')
        >>> lista_lincada.insert_at_tail('b')
        >>> lista_lincada.insert_at_tail('c')
        >>> str(lista_lincada)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])

    def __len__(self):
        """
        >>> lista_lincada = ListaDobleLincada()
        >>> for i in range(0, 5):
        ...     lista_lincada.insert_at_nth(i, i + 1)
        >>> len(lista_lincada) == 5
        True
        """
        return len(tuple(iter(self)))

    def insert_at_head(self, data):
        self.insert_at_nth(0, data)

    def insert_at_tail(self, data):
        self.insert_at_nth(len(self), data)

    def insert_at_nth(self, index: int, data):
        """
        >>> lista_lincada = ListaDobleLincada()
        >>> lista_lincada.insert_at_nth(-1, 666)
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        >>> lista_lincada.insert_at_nth(1, 666)
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        >>> lista_lincada.insert_at_nth(0, 2)
        >>> lista_lincada.insert_at_nth(0, 1)
        >>> lista_lincada.insert_at_nth(2, 4)
        >>> lista_lincada.insert_at_nth(2, 3)
        >>> str(lista_lincada)
        '1->2->3->4'
        >>> lista_lincada.insert_at_nth(5, 5)
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        """
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        nuevo_nodo = Node(data)
        if self.head is None:
            self.head = self.tail = nuevo_nodo
        elif index == 0:
            self.head.previous = nuevo_nodo
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
        elif index == len(self):
            self.tail.next = nuevo_nodo
            nuevo_nodo.previous = self.tail
            self.tail = nuevo_nodo
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            temp.previous.next = nuevo_nodo
            nuevo_nodo.previous = temp.previous
            nuevo_nodo.next = temp
            temp.previous = nuevo_nodo

    def delete_head(self):
        return self.delete_at_nth(0)

    def delete_tail(self):
        return self.delete_at_nth(len(self) - 1)

    def delete_at_nth(self, index: int):
        """
        >>> lista_lincada = ListaDobleLincada()
        >>> lista_lincada.delete_at_nth(0)
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        >>> for i in range(0, 5):
        ...     lista_lincada.insert_at_nth(i, i + 1)
        >>> lista_lincada.delete_at_nth(0) == 1
        True
        >>> lista_lincada.delete_at_nth(3) == 5
        True
        >>> lista_lincada.delete_at_nth(1) == 3
        True
        >>> str(lista_lincada)
        '2->4'
        >>> lista_lincada.delete_at_nth(2)
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        """
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
        """
        >>> lista_lincada = ListaDobleLincada()
        >>> lista_lincada.is_empty()
        True
        >>> lista_lincada.insert_at_tail(1)
        >>> lista_lincada.is_empty()
        False
        """
        return len(self) == 0


def test_lista_doble_lincada() -> None:
    """
    >>> test_lista_doble_lincada()
    """
    lista_lincada = ListaDobleLincada()
    assert lista_lincada.is_empty() is True
    assert str(lista_lincada) == ""

    try:
        lista_lincada.delete_head()
        raise AssertionError()  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    try:
        lista_lincada.delete_tail()
        raise AssertionError()  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(lista_lincada) == i
        lista_lincada.insert_at_nth(i, i + 1)
    assert str(lista_lincada) == "->".join(str(i) for i in range(1, 11))

    lista_lincada.insert_at_head(0)
    lista_lincada.insert_at_tail(11)
    assert str(lista_lincada) == "->".join(str(i) for i in range(0, 12))

    assert lista_lincada.delete_head() == 0
    assert lista_lincada.delete_at_nth(9) == 10
    assert lista_lincada.delete_tail() == 11
    assert len(lista_lincada) == 9
    assert str(lista_lincada) == "->".join(str(i) for i in range(1, 10))




lista_lincada = ListaDobleLincada()
lista_lincada.insert_at_head('b')
lista_lincada.insert_at_head('a')
lista_lincada.insert_at_tail('c')
tuple(lista_lincada)
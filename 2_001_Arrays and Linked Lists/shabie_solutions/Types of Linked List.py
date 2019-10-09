class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node_cursor = self.head
        while node_cursor.next:  # as long as it has an object, keep parsing
            node_cursor = node_cursor.next
        node_cursor.next = Node(value)
        return


class DoubleNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next


dll = DoubleLinkedList()
dll.append(3)
dll.append(4)
dll.append(5)

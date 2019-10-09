class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({self.value})'


class LinkedList(object):

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node_cursor = self.head
        while node_cursor.next:  # as long as it has an object, keep parsing. O(N)
            node_cursor = node_cursor.next
        node_cursor.next = Node(value)
        return

    def prepend(self, value):  # O(1)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def search(self, value):  # O(N)
        node_cursor = self.head
        while node_cursor is not None:
            if node_cursor.value == value:
                return node_cursor
            node_cursor = node_cursor.next
        return node_cursor

    def remove(self, value):
        node_cursor = self.head
        prev_node_cursor = None
        while node_cursor is not None:
            if node_cursor.value == value:
                break
            else:
                prev_node_cursor = node_cursor
                node_cursor = node_cursor.next

        if prev_node_cursor is None:
            self.head = node_cursor.next
        else:
            prev_node_cursor.next = node_cursor.next
        del node_cursor


    def pop(self):  # O(N)
        pop_value = self.head.value
        if self.head.next is not None:
            new_head = self.head.next
            self.head = new_head
        else:
            del self.head

        return pop_value

    def insert(self, value, index):  # O(N)

        if index == 0:
            self.prepend(value)
            return

        prev_node_cursor = None
        node_cursor = self.head

        for i in range(index):
            prev_node_cursor = node_cursor
            node_cursor = node_cursor.next

        # Index lies too far beyond the current list index range
        if prev_node_cursor is None and node_cursor is None:
            raise IndexError

        new_node = Node(value)
        prev_node_cursor.next = new_node
        new_node.next = node_cursor
        return


    def __len__(self):  # O(N)
        node_cursor = self.head
        count = 0
        while node_cursor is not None:
            count += 1
            node_cursor = node_cursor.next
        return count

    def to_list(self):

        list_ = []
        node_cursor = self.head

        while node_cursor:
            list_.append(node_cursor.value)
            node_cursor = node_cursor.next
        return list_


## Test your implementation here

# Test prepend
print('Testing prepend...')
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1,
                                 3], f"list contents: {linked_list.to_list()}"

# Test append
print('Testing append...')
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1,
                                 3], f"list contents: {linked_list.to_list()}"

# Test search
print('Testing search...')
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(
    1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(
    4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
print('Testing remove...')
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4,
                                 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4,
                                 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1,
                                 4], f"list contents: {linked_list.to_list()}"

# Test pop
print('Testing pop...')
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert
print('Testing insert...')
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1,
                                 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1,
                                 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 4)
assert linked_list.to_list() == [5, 2, 1, 4,
                                 3], f"list contents: {linked_list.to_list()}"
# Test size
print('Testing size...')
assert len(linked_list) == 5, f"list contents: {linked_list.to_list()}"

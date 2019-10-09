# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def flatten_deep(self):
        value_list = []
        node = self.head

        while node.next is not None:
            value_list.append(node.value)
            node = node.next
        value_list.append(
            node.value)  # append the last value after exiting out of the loop
        return value_list

    def __eq__(self, other):
        ix = 0
        node = self.head
        while node.next is not None:
            if node.value == other[ix]:
                node = node.next
                ix += 1
            else:
                return False
        return True

    def __repr__(self):
        res = []
        node = self.head
        while node:
            res.append(node.value)
            node = node.next
        return res.__repr__()


class NestedLinkedList(LinkedList):

    @staticmethod
    def merge(a, b):

        if a is None:
            return b
        elif b is None:
            return a

        merged = LinkedList(None)

        na = a.head
        nb = b.head

        while na is not None or nb is not None:

            # if one list is empty, keep appending the 2nd list node by node
            if na is None:
                merged.append(nb)
                nb = nb.next
            elif nb is None:
                merged.append(na)
                na = na.next

            # if both are non-empty, compare 2 values and append the smaller one
            elif na.value <= nb.value:
                merged.append(na)
                na = na.next
            else:
                merged.append(nb)
                nb = nb.next

        return merged

    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is not None:
            return self.merge(node.value, self._flatten(node.next))
        else:
            return self.merge(node.value, None)

# Setup for testing
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)

solution = nested_linked_list.flatten()
print(solution)
assert solution == [1,2,3,4,5]


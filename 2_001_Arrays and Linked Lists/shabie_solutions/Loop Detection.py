# Helper Code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({self.value})'


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:  # Move to the tail (the last node)
            node = node.next

        node.next = Node(value)
        return


def iscircular(ll):

    if ll.head is None:
        return False

    slow = ll.head  # slow pointer
    fast = ll.head  # fast pointer
    while fast.next:  # if LinkedList is non-circular loop will normally exit
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':

    # Creating a loopy LinkedList where last node will point back to 2nd node

    list_with_loop = LinkedList([2, -1, 3, 0, 5])
    loop_start = list_with_loop.head.next  # select the 2nd node

    node = list_with_loop.head
    while node.next:  # go to last node
        node = node.next
    node.next = loop_start  # assign 2nd loop ref. to last one's "next" attr.

    # Test Cases
    small_loop = LinkedList([0])
    small_loop.head.next = small_loop.head
    print("Pass" if iscircular(list_with_loop) else "Fail")
    print("Pass" if not iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
    print("Pass" if not iscircular(LinkedList([1])) else "Fail")
    print("Pass" if iscircular(small_loop) else "Fail")
    print("Pass" if not iscircular(LinkedList([])) else "Fail")

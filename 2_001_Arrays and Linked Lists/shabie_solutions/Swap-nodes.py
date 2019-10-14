class Node:
    """LinkedListNode class to be used for this problem"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'


def swap_nodes(head, i, j):
    assert i != j

    counter = 0
    i_node = prev_i_node = None
    j_node = prev_j_node = None
    node = head
    prev_node = None
    while node:

        if counter == i:
            i_node = node
            prev_i_node = prev_node

        if counter == j:
            j_node = node
            prev_j_node = prev_node

        if (j_node is not None) and (i_node is not None):

            if abs(i - j) > 1:
                i_node.next, j_node.next = j_node.next, i_node.next
                prev_i_node.next, prev_j_node.next = j_node, i_node
            else:
                i_node.next, j_node.next = j_node.next, i_node
                if prev_i_node is not None:
                    prev_i_node.next = j_node
                else:  # if head gets moved to another spot, reassign it
                    head = j_node

            return head

        prev_node = node
        node = node.next
        counter += 1


def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]

    left_node = None
    right_node = None

    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)
        print_linked_list(updated_head)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2
right_index = 4
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

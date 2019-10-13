# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'


def skip_i_delete_j(head, i, j):
    if j == 0:
        return head

    del_cntr = skip_cntr = 1
    skip_cursor = None

    node = head
    while node is not None:
        if skip_cntr < i:
            node = node.next
            skip_cntr += 1
            if skip_cntr == i:
                skip_cursor = node
            continue
        elif del_cntr <= j:
            node = node.next
            del_cntr += 1
            if del_cntr > j:
                if node is None:
                    # not enough values to delete before list reaches end
                    skip_cursor.next = None
                    return head
                else:
                    skip_cursor.next = node.next
                    node.next = None
            continue
        else:
            skip_cntr = del_cntr = 1
            node = skip_cursor.next
    return head


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
        print(head.data, end=' ')
        head = head.next
    print()


def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]

    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
head = create_linked_list(arr)
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 20
j = 3
head = create_linked_list(arr)
solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

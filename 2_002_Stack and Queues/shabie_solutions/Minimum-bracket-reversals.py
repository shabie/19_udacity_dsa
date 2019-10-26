class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of bracket reversals needed
    """

    len_ = len(input_string)

    # Non even length cases can never be balanced
    is_len_odd = (len_ % 2) != 0
    if is_len_odd:
        return -1

    # Correcting extreme cases i.e. first & last brackets if they face opposite
    extra_movements = 0

    if input_string[0] == '}':
        input_string = '{' + input_string[1:]
        extra_movements += 1

    if input_string[len_ - 1] == '{':
        input_string = input_string[:len_ - 1] + '}'
        extra_movements += 1

    prev_char = '-'

    stack = Stack()

    for char in input_string:
        if prev_char + char == '{}':  # remove open one when its balancing "partner" is found
            _ = stack.pop()
            prev_char = stack.top()

            if stack.size() == 0:
                prev_char = '-'  # since None isnt convertd to str -> give a dummy char
        else:
            stack.push(char)  # stack brackets that must be balanced
            prev_char = char

    return int(stack.size() / 2) + extra_movements  # no. of reversals needed


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_3)

test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_4)

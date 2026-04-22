class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
    

    def is_empty(self):
        if self.head == None:
            return True

        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data


    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    

    def pop(self):
        if self.is_empty():
            return None                 
        popped = self.head.data
        self.head = self.head.next
        return popped
#
# time complexity
# push() = o(1)
# pop() = o(1)
# peek() = o(1)
# is_empty() = 0(1)



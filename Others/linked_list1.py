class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_end(self, data):
        node = Node(data, None)

        if self.head == None:
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node

    def insert_at_beginning(self, data):

        if self.head is None:
            node = Node(data)
            self.head = node
            return

        node = Node(data, self.head)
        self.head = node

    def insert_at(self, index, data):
        if index < -1 or index >= self.get_length():
            raise Exception("Index out of range")

        if self.head is None:
            node = Node(data)
            self.head = node
            return

        count = 0
        itr = self.head

        while itr:
            if count == index:
                node = Node(data, itr.next)
                itr.next = node
                return
            count += 1

    def remove_node(self, index):
        count = 0

        if self.head is None:
            print('Linked list is Empty')

        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            count += 1
            itr = itr.next

    def print_linkedlist(self):
        itr = self.head
        while itr:
            print(itr.data, end='-->')

            itr = itr.next
        print()


l = Linked_list()
l.insert_at_end(0)
l.insert_at_end(1)
l.insert_at_end(2)
l.insert_at_end(3)
l.insert_at(2, 1.5)
l.print_linkedlist()

l.remove_node(3)
l.print_linkedlist()

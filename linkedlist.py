class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def  insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_legnth(self):
        count = 0
        itr = self.head
        while itr:

            count += 1
            itr = itr.next
        return count

    def insert_at_position(self, position, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        itr = self.head
        i = 0
        while itr.next:
            if i == position - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            i += 1

    def remove_at(self, position):
        if self.head:
            return
        itr = self.head
        i = 0
        while itr:
            if i == position - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            i += 1

    def print_list(self):
        if self.head is None:
            return "Linked List is empty"
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.val) + '--->'
            itr = itr.next
        return listr

l = LinkedList()
l.insert_at_beginning(3)
l.insert_at_beginning(1)
l.insert_at_end(5)
print(l.get_lenght())
l.insert_at_position(1, 2)
l.remove_at(2)
print(l.print_list())


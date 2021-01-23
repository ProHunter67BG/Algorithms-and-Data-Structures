class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
class DoblyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, val):
        node = Node(val,  None, self.head)
        if self.head != None:
            p = self.head
            p.prev = node
        self.head = node
    def insert_at_end(self, val):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, itr, None)

    def print_dl(self):
        itr = self.head
        p = ''
        while itr:
            p += str(itr.val) + '----->'
            itr = itr.next
        return p
d = DoblyLinkedList()
d.insert_at_beginning(5)
d.insert_at_beginning(3)
d.insert_at_end(12)
print(d.print_dl())
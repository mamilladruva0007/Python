class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkList:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node


 
    def insert_at_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        itr = self.head

        while itr.next is not None:
            itr = itr.next

        itr.next = node


   
    def counter(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count


   
    def insert_at_position(self, data, position):

        if position < 1 or position > self.counter() + 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        if position == self.counter() + 1:
            self.insert_at_end(data)
            return

        node = Node(data)

        itr = self.head
        count = 1

        while count < position - 1:
            itr = itr.next
            count += 1

        node.next = itr.next
        itr.next = node


    
    def delete_at_beginning(self):

        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next



    def delete_at_end(self):

        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        itr = self.head

        while itr.next.next is not None:
            itr = itr.next

        itr.next = None


    def delete_at_position(self, position):

        if self.head is None:
            print("List is empty")
            return

        if position < 1 or position > self.counter():
            print("Invalid position")
            return

       
        if position == 1:
            self.head = self.head.next
            return

        itr = self.head
        count = 1

        while count < position - 1:
            itr = itr.next
            count += 1

        itr.next = itr.next.next


   
    def print_list(self):

        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head

        while itr:
            print(itr.data, end=" -> ")
            itr = itr.next

        print("None")




ll = SingleLinkList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_end(40)
ll.insert_at_position(50, 3)
ll.print_list()
ll.delete_at_beginning()
ll.print_list()
ll.delete_at_end()
ll.print_list()
ll.delete_at_position(2)
ll.print_list()
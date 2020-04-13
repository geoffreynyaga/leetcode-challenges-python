class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next

        last_node.next = new_node

    def pre_append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def append_after_node(self, value, target):

        if self.head == None:
            print("cannot append on an empty list")
            return
        new_node = Node(value)
        last_node = self.head
        while last_node:
            if last_node.data == target:
                new_node.next = last_node.next
                last_node.next = new_node
            last_node = last_node.next


llist = LinkedList()
llist.append("a")
llist.append("b")
llist.append("c")
llist.append("d")
llist.pre_append("e")
llist.append_after_node("f", "c")


llist.print_list()

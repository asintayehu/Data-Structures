class Node:
    def __init__(self, data=None):
        """
        :param: data: value that user wants to initialize node with
        """
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        """
        :param: data: value that user wants to append to end of linked list
        :return: None
        """
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def length(self):
        """
        :return: length of linked list
        """
        current = self.head
        count = 0
        while current.next is not None:
            count += 1
            # increment current node
            current = current.next
        return count

    def display(self):
        """
        :return: Void, just a helper function to visualize the nodes :)
        """
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        """
        :param: index: index that user wants to return, starting from index 0
        :return: value inside of node at the given index
        """
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
        current_index = 0
        current_node = self.head
        while True:
            # increment current node
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def erase(self, index):
        """
        :param: index: index that user wants to delete data at, starting from 0
        :return: Nothing
        """
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        current_index = 0
        current_node = self.head
        while True:
            # save current node as last node
            last_node = current_node
            # increment current node
            current_node = current_node.next
            if current_index == index:
                # set previous node pointer equal to the node adjacent to the current node, deleting the current node
                last_node.next = current_node.next
                return
            current_index += 1


my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list.get(1))

my_list.erase(0)

my_list.display()

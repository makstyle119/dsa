class Node:
    """
    Represents a single node in the linked list.
    """
    def __init__(self, data):
        """
        Initializes a new node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None 

class LinkedList:
    """
    Represents a linked list data structure.
    """
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Adds a new node to the end of the linked list.

        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data) 

        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def print_list(self):
        """
        Prints the data of all nodes in the linked list.
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Example usage
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    my_list.print_list()  # Output: 10 20 30 40
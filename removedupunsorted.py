'''
remove-duplicates-from-an-unsorted-linked-list
Given a linked list, remove the duplicates from the list. The list is unsorted.
You may not use any additional data structures to solve this problem.
You may assume that the list has at least one element and that all elements are integers.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()
# Example usage     
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(2)

    print("Original list:")
    ll.print_list()

    ll.remove_duplicates()

    print("List after removing duplicates:")
    ll.print_list()
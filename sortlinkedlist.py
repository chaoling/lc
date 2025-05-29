'''
How to sort a linked list in Python
This code implements a merge sort algorithm to sort a linked list.
This is a common interview question and can be solved using a recursive approach.
This code defines a `Node` class for the linked list and a `LinkedList` class
that contains methods to insert nodes, merge two sorted lists, and sort the linked list using merge sort.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:   
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data < right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    def get_middle(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        mid = self.get_middle(head)
        next_to_mid = mid.next
        mid.next = None  # Split the list into two halves

        left_half = self.merge_sort(head)
        right_half = self.merge_sort(next_to_mid)

        return self.merge(left_half, right_half)

    def sort(self):
        self.head = self.merge_sort(self.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' -> '.join(result)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(4)
    ll.insert(2)
    ll.insert(1)
    ll.insert(3)
    
    print("Original linked list:")
    ll.print_list()
    
    ll.sort()
    
    print("\nSorted linked list:")
    ll.print_list()
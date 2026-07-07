# Middle of a Linked List
"""
Question. 
    Find the middle of a given linked list. 
    Input: 0 1 2 3 4
    Output: 2
    If the number of nodes are even, return the second middle node.
    Input: 0 1 2 3 4 5
    Output: 3
 """

class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next
    
def middle_of_linked_list(head: Node) -> int:
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
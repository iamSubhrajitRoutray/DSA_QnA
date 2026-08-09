'''Reverse a Linked List
Q)
Given the head of a singly linked list,
write a program to reverse the linked list, and return the head pointer to the reversed list.'''



'''OPTIMAL APPROACH'''

class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
def reversal(head):
    
    prev = None
    curr = head
    
    while head is not None:
        
        front = curr.next
        
        curr.next = prev

        prev = curr
        
        curr = front
    
    return prev



def print_ll(head):
    
    while head:
        
        print(head.val, end=" ")
        
        head = head.next
        
    print()
    
    
    
# Main/Driver code:

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
           
answer = print_ll(head)
print_ll(answer)




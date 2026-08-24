'''Reverse a Linked List
Q)
Given the head of a singly linked list,
write a program to reverse the linked list, and return the head pointer to the reversed list.'''



'''OPTIMAL APPROACH'''

class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
     
        
def reversal_ll(head):
    
    curr = head
    
    prev = None
    
    
    while curr is not None:
        
        front = curr.next      # Save the next node
        
        curr.next = prev       # Reverse the link
        
        prev = curr            # Move the prev
        
        curr = front           # Move the curr
        
    return prev



def print_ll(head):
    
    while head:
        
        print(head.val, end=" ")
        
        head = head.next
        
    print()
    
    
    
# Main/Driver code:


head = Node(5)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
           
answer = reversal_ll(head)
print_ll(answer)




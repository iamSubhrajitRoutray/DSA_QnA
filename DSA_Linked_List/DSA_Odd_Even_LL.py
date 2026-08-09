'''Segregate even and odd nodes in LinkedList
Q)
Given the head of a singly linked list.
Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list.
Consider the 1st node to have index 1 and so on.
The relative order of the elements inside the odd and even group must remain the same as the given input.'''




'''OPTMAL APPROACH'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

def segregate_odd_even(head):
    
    odd = head
    even = head.next
    even_head = even
    
    while even is not None and even.next is not None:
        
        odd.next = odd.next.next
        odd = odd.next
        
        even.next = even.next.next
        even = even.next
        
    odd.next = even_head
    
    return head


def print_segregate_ll(head):
    
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
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)


answer = segregate_odd_even(head)

print_segregate_ll(answer)
        
        
    
    
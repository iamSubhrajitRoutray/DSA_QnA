'''Remove duplicates from sorted DLL
Q)
Given the head of a doubly linked list with its values sorted in non-decreasing order.
Remove all duplicate occurrences of any value in the list so that only distinct values are present in the list.
Return the head of the modified linked list.'''


class Node:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
        
def removal(head):
    
    current = head
    
    while current:
        
        if current.prev is not None and current.prev.val == current.val:
            
            if current.prev == head:
                
                current.prev = None
                head = current
                
            else:
                
                current.prev.prev.next = current.next
                current.next.prev = current.prev.prev
                
        current = current.next
        
    return head



def print_DLL(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()
    
    

# MAIN/DRIVER CODE :

head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(3)
fifth = Node(5)
sixth = Node(6)

head.next = second

second.prev = head
second.next = third

third.prev = second
third.next = fourth

fourth.prev = third
fourth.next = fifth

fifth.prev = fourth
fifth.next = sixth

sixth.prev = fifth


ans = removal(head)
print_DLL(ans)
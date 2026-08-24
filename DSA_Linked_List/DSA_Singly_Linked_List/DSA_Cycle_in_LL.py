'''Detect a Cycle in a Linked List
Q)
Given a Linked List, determine whether the linked list contains a cycle or not.'''



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    
'''BRUTE-FORCE APPROACH'''


def has_cycle(head):
    
    temp = head
    myset = set()
    
    while temp is not None:
    
        if temp in myset:
            return True
    
        myset.add(temp)
    
        temp = temp.next
    
    return False



# Main/Driver code:    
    
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

fifth.next = None

answer = has_cycle(head)

if answer:
    print("The Cycle has been detected in the Linked List")
else:
    print("Loop has not been detected in the Linked List")
    



'''OPTIMAL APPROACH'''


def has_loop(head):
    
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        
        slow = slow.next
        fast = fast.next.next
        
        if fast == slow:
            return True
    
    return False



# Main/Driver code:    
    
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

fifth.next = third

answer = has_loop(head)

if answer:
    print("Cycle/Loop has been detected in the Linked List")
else:
    print("Loop has not been detected in the Linked List")
    
    
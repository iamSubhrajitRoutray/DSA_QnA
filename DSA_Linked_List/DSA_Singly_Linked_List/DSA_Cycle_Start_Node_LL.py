'''Starting point of loop in a Linked List
Q)
Given the head of a linked list that may contain a cycle, return the starting point of that cycle.
If there is no cycle in the linked list return null.'''




class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



'''BRUTE-FORCE APPROACH'''


def cycle_start_node(head):
    
    curr = head
    
    my_set = set()
    
    while curr is not None:
        if curr in my_set:
            return curr
        
        my_set.add(curr)
        curr = curr.next
    return None


# Main/Driver code:    
    
head = Node(11)
second = Node(22)
third = Node(33)
fourth = Node(44)
fifth = Node(55)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

fifth.next = third

answer = cycle_start_node(head)

if answer:
    print(f"The starting node of the cycle: {answer.val}")
else:
    print(f"Loop has not been detected in the Linked List")
    
        
        
'''OPTIMAL APPROACH'''
        
        
def starting_node(head):
    
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            slow = head
            
            while slow != fast:
                
                slow = slow.next
                fast = fast.next
                
            return slow
   
    return None


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

answer = starting_node(head)

if answer:
    print(f"The starting node of the cycle: {answer.val}")
else:
    print(f"Loop has not been detected in the Linked List")


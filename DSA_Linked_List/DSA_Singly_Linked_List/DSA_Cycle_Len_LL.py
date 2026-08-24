'''Length of Loop in Linked List
Q)
Given the head of a linked list,
determine the length of a loop present in the linked list. If there's no loop present, return 0.'''




class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
'''BRUTE FORCE APPROACH'''

        
def find_cycle_len(head):
    
    my_dict = dict()
    
    temp = head
    
    travel = 1
    
    while temp is not None:
        
        if temp in my_dict:
            
            return travel - my_dict[temp]
        
        my_dict[temp] = travel
        
        travel += 1
        
        temp = temp.next
        
    return temp



# Main/Driver code:    
    
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

sixth.next = third

answer = find_cycle_len(head)

if answer:
    print(f"The lenght of the loop : {answer}")
else:
    print("Loop has not been detected in the Linked List")
    
    
    
    
    
'''OPTIMAL APPROACH'''


def len_of_cycle(head):
    
    slow, fast = head, head
    
    while fast is not None and fast.next is not None:
        
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            
            fast = fast.next
            
            count = 1
            
            while fast != slow:
            
                fast = fast.next
                count += 1
            
            return count
    
    return None




# Main/Driver code:    
    
head = Node(12)
second = Node(21)
third = Node(32)
fourth = Node(44)
fifth = Node(54)
sixth = Node(65)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

sixth.next = third

answer = len_of_cycle(head)

if answer:
    print(f"The lenght of the cycle : {answer}")
else:
    print("Loop has not been detected in the Linked List")
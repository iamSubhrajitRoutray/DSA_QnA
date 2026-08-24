'''Find middle element in a Linked List
Q)
Given the head of a linked list of integers, determine the middle node of the linked list.
However, if the linked list has an even number of nodes, return the second middle node.'''


class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
        

'''BRUTE-FORCE APPROACH'''


def get_lenght(head):
    
    lenght = 0
    temp = head
    
    while temp is not None:
        
        lenght += 1

        temp = temp.next
        
    return lenght


def get_middle_node(head):
    
    lenght = get_lenght(head)
    
    middle_index = lenght // 2
    
    for _ in range(0, middle_index):
        head = head.next
    return head



# Main/Driver code:

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
           
middle_node = get_middle_node(head)
print(f"The middle of the Linked List is : {middle_node.val}")






'''OPTIMAL (TORTOISE-HARE) APPROACH'''

        
def find_middle_node(head):
    
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        
        slow = slow.next
        fast = fast.next.next
        
    return slow


# Main/Driver code:

head = Node(18)
head.next = Node(21)
head.next.next = Node(35)
head.next.next.next = Node(40)
head.next.next.next.next = Node(57)
head.next.next.next.next.next = Node(62)
           
middle_node = find_middle_node(head)
print(f"The middle of the Linked List is : {middle_node.val}")





'''Remove Nth Node from End of List | Two Pointer Approach'''



class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
def removal(n, head):
    
    lenght = 0
    
    temp = head
    
    
    while temp is not None:
        
        lenght += 1
        
        temp = temp.next
        
    if lenght == n:
    
        new_head = head.next
        
        del head
    
        return new_head
    
    
    stop_position = lenght - n
    
    temp = head
    
    count = 1
    
    
    while count < stop_position:
        
        temp = temp.next
        
        count += 1
        
    temp.next = temp.next.next
    
    return head


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

n_node = int(input("Enter the Node to remove: "))

answer = removal(n_node, head)

print_ll(answer) 



'''OPTIMAL APPROACH'''

def remove_n_node(n, head):
    
    slow, fast = head, head
    
    for _ in range(n):
        
        fast = fast.next
    
    
    if fast == None:
        
        new_head = head.next
        
        return new_head
    
    
    while fast.next is not None:
        
        slow = slow.next
        
        fast = fast.next
    
    slow.next = slow.next.next
    
    return head
    

def print_linkedlist(head):
    
    while head:
    
        print(head.val, end=" ")
    
        head = head.next
    
    print()



# Main/Driver code:

head = Node(11)
head.next = Node(22)
head.next.next = Node(33)
head.next.next.next = Node(44)
head.next.next.next.next = Node(55)

n_node = int(input("Enter the Node to remove: "))

answer = remove_n_node(n_node, head)

print_linkedlist(answer)    

        
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def doSomething(headA, headB):
    # Create a dummy node to simplify the code for merging two linked lists
    dummy = ListNode()
    # Initialize the current pointer to the dummy node
    current = dummy

    # Iterate while both linked lists have elements
    while headA is not None and headB is not None:
        # Compare values of the current nodes in both lists
        if headA.value < headB.value:
            # If the value in list A is smaller, link the current node to list A
            current.next = headA
            headA = headA.next
        else:
            # If the value in list B is smaller or equal, link the current node to list B
            current.next = headB
            headB = headB.next
        # Move the current pointer to the last added node
        current = current.next

    # Check if there are remaining nodes in list A or list B
    if headA is not None:
        current.next = headA
    elif headB is not None:
        current.next = headB

    # Return the merged linked list starting from the next of the dummy node
    return dummy.next

# Function to create a linked list from a list of values
def create_linked_list(count, values):
    if count == 0:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to print a linked list
def print_linked_list(head):
    while head is not None:
        print(head.value)
        head = head.next

# Input from the user
count_A = int(input("Enter the count for List A: "))
values_A = [int(input()) for _ in range(count_A)]

count_B = int(input("Enter the count for List B: "))
values_B = [int(input()) for _ in range(count_B)]

# Create linked lists
headA = create_linked_list(count_A, values_A)
headB = create_linked_list(count_B, values_B)

# Perform the operation to merge two sorted linked lists
merged_head = doSomething(headA, headB)

# Print the result
print("Merged Linked List:")
print_linked_list(merged_head)

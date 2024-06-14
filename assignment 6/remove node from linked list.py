class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def removeNodes(head):
    head = reverseList(head)
    
    stack = []
    dummy = ListNode(0)
    curr = dummy
    
    while head:
        if not stack or head.val >= stack[-1]:
            stack.append(head.val)
            curr.next = ListNode(head.val)
            curr = curr.next
        head = head.next
    
    return reverseList(dummy.next)

def createLinkedList(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head = createLinkedList([5, 2, 13, 3, 8])
new_head = removeNodes(head)
print(linkedListToList(new_head))  

head = createLinkedList([1, 1, 1, 1])
new_head = removeNodes(head)
print(linkedListToList(new_head)) 
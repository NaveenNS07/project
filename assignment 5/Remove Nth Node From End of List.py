class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    for i in range(1, n+2):
        first = first.next
    
    while first is not None:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    
    return dummy.next
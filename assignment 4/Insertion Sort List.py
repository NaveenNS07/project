class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head):
    if not head or not head.next:
        return head
    dummy = ListNode(0)
    dummy.next = head
    curr = head
    prev = dummy
    
    while curr:
        if curr.next and curr.next.val < curr.val:
            while prev.next and prev.next.val < curr.next.val:
                prev = prev.next
            
            temp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = temp
            
            prev = dummy
        else:
            curr = curr.next
    
    return dummy.next
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

print("Original list:")
printList(head)

sorted_head = insertionSortList(head)

print("Sorted list:")
printList(sorted_head)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

dummy = ListNode(0)
current = dummy
carry = 0

while l1 or l2 or carry:
    if l1:
        carry += l1.val
        l1 = l1.next
    if l2:
        carry += l2.val
        l2 = l2.next
    current.next = ListNode(carry % 10)
    current = current.next
    carry //= 10

result = dummy.next
while result:
    print(result.val, end=" ")
    result = result.next
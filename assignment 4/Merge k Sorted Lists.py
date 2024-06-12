from heapq import heappop, heappush
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):  
        return self.val < other.val

def mergeKLists(lists):
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heappush(heap, lists[i])
    dummy = ListNode()
    current = dummy
  
    while heap:  
        node = heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heappush(heap, node.next)
    return dummy.next

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode (4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]

merged_list = mergeKLists(lists)
printList(merged_list)

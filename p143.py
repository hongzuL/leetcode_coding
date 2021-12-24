# 143. Reorder List
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        if not head.next or not head.next.next:
            return
        # find the mid point
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            # print(slow.val, fast.val)
        mid = slow.next
        slow.next = None # detach list on the middle
        # flip the second half
        self.printList(head)
        print("---------------")
        self.printList(mid)
        prev, curr, next = None, mid, None
        while curr: 
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        print("---------------")
        self.printList(prev)
        # join first half and second half
        second = prev
        dummy = ListNode(0)
        tail = dummy
        last_node = 1
        while head or second:
            if last_node == 1:
                tail.next = head
                head = head.next
                last_node = 0
            elif last_node == 0:
                tail.next = second
                second = second.next
                last_node = 1
            tail = tail.next
        dummy = dummy.next
        print("---------------")
        self.printList(dummy)

    def printList(self, head):
        while head is not None:
            print(head.val)    
            head = head.next
def createLinkedlist(imp, i, head):
    if i == len(imp):
        return
    val = inp[i]
    tmp = ListNode(val,None)
    head.next = tmp
    createLinkedlist(imp, i+1, head.next)
    return head

inp = [1,2,3,4,5,6]
head = ListNode(inp[0],None)
head = createLinkedlist(inp, 1, head)

solution = Solution()
solution.reorderList(head)
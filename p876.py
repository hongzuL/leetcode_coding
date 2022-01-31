# 876. Middle of the Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        mid_node = head
        end_node = head
        count = self.lenLinkedList(head)
        while end_node.next and end_node.next.next:
            mid_node = mid_node.next
            end_node = end_node.next.next
        if count % 2 == 0:
            mid_node = mid_node.next
        self.printLinkedList(mid_node)

    def lenLinkedList(self, head):
        tmp = head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def createLinkedList(self, list_vals):
        tmp = ListNode()
        head = tmp
        for i in range(len(list_vals)):
            tmp.val = list_vals[i]
            if i >= len(list_vals) - 1:
                tmp.next = None
            else:
                tmp.next = ListNode()
                tmp = tmp.next
        return head
    
    def printLinkedList(self, head):
        tmp = head
        while tmp:
            print(tmp.val)
            tmp = tmp.next
    
head = [1,2,3,4,5, 6]
solution = Solution()
head = solution.createLinkedList(head)
solution.printLinkedList(head)
print("------")
solution.middleNode(head)
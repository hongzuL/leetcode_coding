#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution:
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        last_node = ListNode(head.val, None)
        while head.next:
            curr_node = ListNode()
            curr_node.next = last_node
            curr_node.val = head.next.val
            head = head.next
            last_node = curr_node
        return curr_node
    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
    
# @lc code=end


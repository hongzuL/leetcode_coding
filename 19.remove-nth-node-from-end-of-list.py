#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_dict = {}
        temp = head
        curr = 0
        while temp:
            head_dict[curr] = temp
            curr += 1
            temp = temp.next
        
        if curr-n == 0:
            return head.next
        else:
            remove_head = head_dict[curr-n-1]
            remove_head.next = remove_head.next.next
            return head

   
# @lc code=end


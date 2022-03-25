# @before-stub-for-debug-begin
from python3problem142 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_dict = {}
        while head:
            if head in visited_dict:
                return head
            visited_dict[head] = True
            head = head.next
        return None
# @lc code=end


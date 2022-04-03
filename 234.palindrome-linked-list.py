#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        listval = list()
        listlen = 0
        while head:
            listval.append(head.val)
            head = head.next
            listlen += 1
        for i in range(listlen // 2):
            if listval[i] != listval[listlen - i - 1]:
                return False
        return True
# @lc code=end


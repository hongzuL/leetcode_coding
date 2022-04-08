#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = rigßht
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            # this is a leaf node
            targetSum -= root.val
            if targetSum == 0:
                return True
            else:
                return False
        # going left
        has_sum = self.hasPathSum(root.left, targetSum-root.val)
        if has_sum:
            return has_sum
        # going right
        has_sum = self.hasPathSum(root.right, targetSum-root.val)
        return has_sum

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        level_nodes = [[root,targetSum]]
        curr_level = 0
        i = 0
        have_node = False
        while i < 2 ** curr_level:
            node = level_nodes[i][0]                
            print(level_nodes)
            if node:
                curr_sum = level_nodes[i][1]-node.val
                if not node.left and not node.right:
                    if curr_sum == 0:
                        return True
                else:    
                    have_node = True
                level_nodes.append([node.left,curr_sum])
                level_nodes.append([node.right,curr_sum])
            else:
                level_nodes.append([None,None])
                level_nodes.append([None,None])
            i += 1
            if i==2**curr_level:
                level_nodes = level_nodes[2**curr_level:]
                curr_level += 1
                i = 0
                if not have_node: 
                    break
                have_node = False
        return False
# @lc code=end


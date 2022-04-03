#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from re import L


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        orig_root = root
        tree_dict = dict()   
        level_nodes = [root]
        curr_level = 0
        # tree_dict[curr_level] = level_nodes
        i = 0
        have_node = False
        while i < 2 ** curr_level:
            # print(level_nodes)
            node = level_nodes[i]
            if node:
                level_nodes.append(node.left)
                level_nodes.append(node.right)
                have_node = True
            else:
                level_nodes.append(None)
                level_nodes.append(None)
            i += 1
            if i==2**curr_level:
                tree_dict[curr_level] = level_nodes[0:i]
                level_nodes = level_nodes[2**curr_level:]
                curr_level += 1
                i = 0
                if not have_node: 
                    break
                have_node = False
        total_level = curr_level -1
        total_nodes = 2**(total_level) - 1
        result = [-1]*total_nodes
        for l in tree_dict.keys():
            if l < total_level:
                for i in range(len(tree_dict[l])):
                    index = 2**(total_level-l-1) + i*2**(total_level-l)
                    # print(l,'->',i,'->',index,'->',len(tree_dict[l]))
                    if tree_dict[l][i]:
                        result[index-1] = tree_dict[l][i].val
                    else:
                        result[index-1] = None
        
        i = 0
        while i < len(result):
            if result[i] == None:
                result.pop(i)
            else:
                i += 1
        return result

        
                
# @lc code=end


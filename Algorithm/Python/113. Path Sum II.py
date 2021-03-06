# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-04 10:18:35
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-04 10:18:45
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result, candidate = [], []
        self.helper(root, sum, 0, candidate, result)
        return result
        
        
    def helper(self, root, sum, count, candidate, result):
        if root == None:
            return  
        if sum == count+root.val and root.left == None and root.right == None:
            candidate.append(root.val)
            result.append(candidate[:])
            candidate.pop()
            return
        candidate.append(root.val)
        self.helper(root.left,  sum, count + root.val, candidate, result)
        self.helper(root.right, sum, count + root.val, candidate, result)
        candidate.pop()
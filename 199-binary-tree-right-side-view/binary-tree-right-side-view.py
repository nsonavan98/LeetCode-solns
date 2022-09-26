# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        glist = []
        maxlevel = [0]
        def printrt(root,level):
            
            if root is None:
                return 
            
            level = level +1
            if level > maxlevel[0] :
                glist.append(root.val)
                maxlevel[0] = level
            
            printrt(root.right,level)
            printrt(root.left,level)
            
        printrt(root,0)
        return glist
            

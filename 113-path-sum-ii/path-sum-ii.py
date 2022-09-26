# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        glist = []
        
        def path(root,tlist,nsum,tsum):
            
            if root is None:
                return 
            
            nsum = nsum + root.val
            tlist.append(root.val)
            #rint(tlist)
            #rint(nsum)
            if root.left is None and root.right is None:
                if nsum == tsum:
                    xlist = tlist.copy()
                    glist.append(xlist)
            
            path(root.left,tlist,nsum,tsum)
            path(root.right,tlist,nsum,tsum)
            #rint("pop")
            tlist.pop()
            
            
        path(root,[],0,targetSum)
        return glist
                    
            

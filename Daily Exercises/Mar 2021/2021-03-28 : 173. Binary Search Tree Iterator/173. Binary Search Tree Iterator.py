# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.s=[root]
        while(self.s[-1].left):
            self.s.append(self.s[-1].left)


    def next(self) -> int:        
        ans=self.s.pop()
        if ans.right:
            self.s.append(ans.right)
            while(self.s[-1].left):
                self.s.append(self.s[-1].left)
        return ans.val
        

    def hasNext(self) -> bool:
        return bool(self.s)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

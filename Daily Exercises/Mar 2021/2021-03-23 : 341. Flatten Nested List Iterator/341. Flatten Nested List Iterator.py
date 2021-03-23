# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # store the reversed 'nestedList'
        self.s=nestedList[::-1]
    
    def next(self) -> int:
        # 'hasNext' ensures the top is interger
        # and thus return top directly
        return self.s.pop().getInteger()
    
    def hasNext(self) -> bool:
        # if the top element is nestedlist
        # pop it and reverse it and then push it back
        # until the top is integer
        while len(self.s) and not self.s[-1].isInteger():
            self.s+=self.s.pop().getList()[::-1]
        return bool(len(self.s))


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

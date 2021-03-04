# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=l1
        b=l2
        t=0
        h=ListNode(0)
        na=h
        while(a or b):
            va,a=(a.val,a.next) if a else (0,a)
            vb,b=(b.val,b.next) if b else (0,b)
            new=va+vb+t
            new,t=(new,0) if new<10 else (new-10,1)
            node=ListNode(new)
            na.next,na=node,node
        if t==1:
            node=ListNode(1)
            na.next=node
        return h.next

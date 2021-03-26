# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p=head
        if p is None or p.next is None:
            return p
        if p.val==p.next.val:
            while(p and p.val==head.val):
                p=p.next
            head.next=self.deleteDuplicates(p)
            return head
        else:
            p.next=self.deleteDuplicates(p.next)
            return p

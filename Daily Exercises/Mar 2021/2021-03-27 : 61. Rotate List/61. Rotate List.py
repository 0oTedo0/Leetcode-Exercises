# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not k or not head or not head.next: return head
        fast=head
        slow=head
        for i in range(k):
            if fast.next:
                fast=fast.next
            else:
                fast=head
                break
        if fast==head:    
            for j in range(k%(i+1)):
                fast=fast.next
        if fast==head:
            return head
        while fast.next:
            fast=fast.next
            slow=slow.next
        ans=slow.next
        fast.next=head
        slow.next=None
        return ans

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        pre=None
        p=head
        for i in range(1,left):  # go to the "left" position
            pre=p
            p=p.next
        
        post=p.next    
        new_tail=p  # record the new tail within the reversed list
        for i in range(left,right):
            temp=post.next  # record the next one
            post.next=p  # the next is changed
            p=post  # step forward
            post=temp  # step forward
        
        new_tail.next=post  # update new tail's next
        if pre:  # if the head is not reversed
            pre.next=p  # concatenate two lists
            return head
        else:
            return p  # else it is the head

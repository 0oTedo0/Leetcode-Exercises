/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode pre=new ListNode(621),p=head;  // Note that the "val" of the dummy node should be out of the range of values of normal nodes, 
                                                // otherwise it is likely to be not able to tell whether a node is dummy.
        for(int i=1;i<left;i++){  // go to the "left" position
            pre=p;
            p=p.next;
        }
        
        ListNode post=p.next;
        ListNode new_tail=p;  // record the new tail within the reversed list
        for(int i=left;i<right;i++){
            ListNode temp=post.next;  // record the next one
            post.next=p;  // the next is changed
            p=post;  // step forward
            post=temp;  // step forward
        }
        
        new_tail.next=post;  // update new tail's next
        if(pre.val!=621){ // if the head is not reversed
            pre.next=p;  // concatenate two lists
            return head;
        }else{
            return p;  // else it is the head
        }    
    }
}

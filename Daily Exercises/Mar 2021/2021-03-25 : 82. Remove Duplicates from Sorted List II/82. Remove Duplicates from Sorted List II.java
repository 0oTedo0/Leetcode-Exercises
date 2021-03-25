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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode p=head;
        if(p==null || p.next==null){
            return p;
        }
        if(p.val==p.next.val){
            while(p!=null && p.val==head.val){
                p=p.next;
            }
            return deleteDuplicates(p);
        }else{
            p.next=deleteDuplicates(p.next);
            return p;
        }
    }
}

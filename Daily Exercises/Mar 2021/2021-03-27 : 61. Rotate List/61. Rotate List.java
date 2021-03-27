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
    public ListNode rotateRight(ListNode head, int k) {
        if(k==0 || head==null || head.next==null){
            return head;
        }
        ListNode fast=head,slow=head;
        int i=0;
        for(;i<k;i++){
            if(fast.next!=null){
                fast=fast.next;
            }else{
                fast=head;
                break;
            }
        }
        if(fast==head){
            for(int j=0;j<k%(i+1);j++){
            fast=fast.next;
            }
        }
        if(fast==head){
            return head;
        }
        while(fast.next!=null){
            fast=fast.next;
            slow=slow.next;
        }
        ListNode ans=slow.next;
        fast.next=head;
        slow.next=null;
        return ans;
    }
}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(!k || head==nullptr || head->next==nullptr){
            return head;
        }
        ListNode* fast=head,*slow=head;
        int i=0;
        for(;i<k;i++){
            if(fast->next!=nullptr){
                fast=fast->next;
            }else{
                fast=head;
                break;
            }
        }
        if(fast==head){
            for(int j=0;j<k%(i+1);j++){
            fast=fast->next;
            }
        }
        if(fast==head){
            return head;
        }
        while(fast->next!=nullptr){
            fast=fast->next;
            slow=slow->next;
        }
        ListNode* ans=slow->next;
        fast->next=head;
        slow->next=nullptr;
        return ans;
    }
};

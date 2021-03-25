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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* p=head;
        if(p==nullptr || p->next==nullptr){
            return p;
        }
        if(p->val==p->next->val){
            while(p!=nullptr && p->val==head->val){
                p=p->next;
            }
            return deleteDuplicates(p);
        }else{
            p->next=deleteDuplicates(p->next);
            return p;
        }
    }
};

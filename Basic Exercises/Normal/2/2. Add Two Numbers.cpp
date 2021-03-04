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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *a=l1,*b=l2;
        int va,vb,newv,t=0;
        auto h= new ListNode(0);
        auto na=h;
        while(a!=nullptr or b!=nullptr){
            if(a!=nullptr){
                va=a->val;
                a=a->next;
            }else{
                va=0;
            }
            if(b!=nullptr){
                vb=b->val;
                b=b->next;
            }else{
                vb=0;
            }
            newv=va+vb+t;
            if(newv<10){
                t=0;
            }else{
                t=1;
                newv=newv-10;
            }
            auto node=new ListNode(newv);
            na->next=node;
            na=node;
        }
        if(t==1){
            auto node=new ListNode(1);
            na->next=node;
        }
        return h->next;
    }
};

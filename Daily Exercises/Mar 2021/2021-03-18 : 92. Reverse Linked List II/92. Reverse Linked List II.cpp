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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* pre=nullptr,*p=head;
        for(int i=1;i<left;i++){  // go to the "left" position
            pre=p;
            p=p->next;
        }
        
        ListNode* post=p->next;
        ListNode* new_tail=p;  // record the new tail within the reversed list
        for(int i=left;i<right;i++){
            ListNode* temp=post->next;  // record the next one
            post->next=p;  // the next is changed
            p=post;  // step forward
            post=temp;  // step forward
        }
        
        new_tail->next=post;  // update new tail's next
        if(pre){ // if the head is not reversed
            pre->next=p;  // concatenate two lists
            return head;
        }else{
            return p;  // else it is the head
        }         
    }
};

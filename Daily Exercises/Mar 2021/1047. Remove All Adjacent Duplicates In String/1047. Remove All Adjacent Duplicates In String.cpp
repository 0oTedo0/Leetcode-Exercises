class Solution {
public:
    string removeDuplicates(string S) {
        string s;   // use string as a stack
        for(auto &item:S){
            if(!s.empty() and s.back()==item){ 
                s.pop_back();  // cancel it out
            }else{
                s.push_back(item);
            }
        }
        return s;
    }
};

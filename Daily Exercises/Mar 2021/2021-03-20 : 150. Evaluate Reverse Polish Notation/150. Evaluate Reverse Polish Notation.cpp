class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for(auto &item:tokens){
            if(isNumber(item)){
                s.push(atoi(item.c_str()));
            }else{
                int top1=s.top();
                s.pop();
                int top2=s.top();
                s.pop();
                switch(item[0]){
                    case '+':
                        s.push(top2+top1);
                        break;
                    case '-':
                        s.push(top2-top1);
                        break;
                    case '*':
                        s.push(top2*top1);
                        break;
                    case '/':
                        s.push(top2/top1);
                        break;
                }
            }
        }
        return s.top();
    }

    bool isNumber(string& token) {
        return !(token == "+" || token == "-" || token == "*" || token == "/");
    }
};

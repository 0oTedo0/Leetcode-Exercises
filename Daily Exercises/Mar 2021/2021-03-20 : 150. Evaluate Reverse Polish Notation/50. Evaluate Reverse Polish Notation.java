class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> s = new LinkedList<Integer>();
        for(String item:tokens){
            if(isNumber(item)){
                s.push(Integer.parseInt(item));
            }else{
                int top1=s.pop();
                int top2=s.pop();
                switch(item){
                    case "+":
                        s.push(top2+top1);
                        break;
                    case "-":
                        s.push(top2-top1);
                        break;
                    case "*":
                        s.push(top2*top1);
                        break;
                    case "/":
                        s.push(top2/top1);
                        break;
                }
            }
        }
        return s.pop();
    }

    public boolean isNumber(String token) {
         return !("+".equals(token) || "-".equals(token) || "*".equals(token) || "/".equals(token));
    }
}

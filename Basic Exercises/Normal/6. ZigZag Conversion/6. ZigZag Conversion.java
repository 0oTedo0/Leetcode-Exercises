class Solution {
    public String convert(String s, int numRows) {
        if(numRows==1){
            return s;
        }
        StringBuilder ans=new StringBuilder();
      
        int n=s.length();
        int cycle=2*numRows-2;
      
        for(int i=0;i<numRows;i++){
            int j=i;
            while(j<n){
                ans.append(s.charAt(j));
                if(i!=0 && i!=numRows-1 && j+cycle-2*i<n){  // rows are visited twice except for the first and the last row
                    ans.append(s.charAt(j+cycle-2*i));
                }
                j+=cycle;
            }
        }
        return ans.toString();
    }
}

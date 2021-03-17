class Solution {
public:
    int numDistinct(string s, string t) {
        int m=s.size(),n=t.size();
        if(m < n){
            return 0;
        }
        vector<vector<long>> dp(m+1, vector<long>(n+1));  // initialization
        for(int i=0;i<m+1;i++){
            dp[i][n]=1;
        }
        
        for(int i=m-1;i>=0;i--){
            for(int j=n-1;j>=0;j--){
                if(s[i]==t[j]){  // transform formula
                    dp[i][j]=dp[i+1][j+1]+dp[i+1][j];
                }else{
                    dp[i][j]=dp[i+1][j];
                }
            }
        }

        return dp[0][0];
    }
};

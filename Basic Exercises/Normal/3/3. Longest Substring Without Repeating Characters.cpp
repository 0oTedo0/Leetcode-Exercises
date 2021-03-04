class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start=0,n=s.size();
        map<char,int> dict;
        int ans=n?1:0;
        for(int i=0;i<n;i++){
            if(dict.count(s[i])){
                ans=max(ans,i-max(start-1,dict[s[i]]));
                start=max(start,dict[s[i]]+1);
            }else{
                ans=max(ans,i-start+1);
            }
            dict[s[i]]=i;
        }
        return ans;
    }
};

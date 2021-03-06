class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start=0,n=s.size();
        map<char,int> dict;
        int ans=n?1:0;
        for(int i=0;i<n;i++){
            if(dict.count(s[i])){
                           // Once we find the repeated letter, we count the length
                           // There are three cases
                           // 1. The start is exactly the repeated letter, len=i-start=i-dict[s[i]]
                           // 2. The repeated letter lies on the right of start, len=i-dict[s[i]]
                           // 3. The repeated letter lies on the left of the start, len=i-start+1
                ans=max(ans,i-max(start-1,dict[s[i]]));
                start=max(start,dict[s[i]]+1);  // Update start to the rightmost of repeated letter
            }else{
                ans=max(ans,i-start+1);  // Update the latest position of a certain letter
            }
            dict[s[i]]=i;
        }
        return ans;
    }
};

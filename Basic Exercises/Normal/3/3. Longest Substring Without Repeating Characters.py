class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        d=dict()
        n=len(s)
        ans=1 if n else 0
        for i in range(n):
            if s[i] in d:
                ans=max(ans,i-max(start-1,d[s[i]]))
                start=max(start,d[s[i]]+1)
            else:
                ans=max(ans,i-start+1)
            d[s[i]]=i

        return ans

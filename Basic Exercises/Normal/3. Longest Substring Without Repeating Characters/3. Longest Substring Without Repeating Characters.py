class Solution:
    def lengthOfLongestSubstring(self, s):
        start=0
        d=dict()
        n=len(s)
        ans=1 if n else 0
        for i in range(n):
            if s[i] in d:  # Once we find the repeated letter, we count the length
                           # There are three cases
                           # 1. The start is exactly the repeated letter, len=i-start=i-d[s[i]]
                           # 2. The repeated letter lies on the right of start, len=i-d[s[i]]
                           # 3. The repeated letter lies on the left of the start, len=i-start+1
                ans=max(ans,i-max(start-1,d[s[i]]))  # This sentence can be replaced by
                                                     # begin,increament=(d[s[i]],0) if d[s[i]]>=start else (start,1)
                                                     # ans=max(ans,i-begin+increament)
                start=max(start,d[s[i]]+1)  # Update start to the rightmost of repeated letter
            else:
                ans=max(ans,i-start+1)
            d[s[i]]=i  # Update the latest position of a certain letter

        return ans

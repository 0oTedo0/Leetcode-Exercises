class Solution:
    def longestPalindrome(self, s):
        n=len(s)
        if n<2:
            return s
        array=[[True for j in range(n)] for i in range(n)]  # array for DP
        maximum=1
        start=0
        for i in range(1,n):  # note that when you are dealing with substring S, all substrings of S need to have been processed already
            for j in range(n-i):
                l=j
                r=j+i
                array[l][r]=(s[l]==s[r]) and array[l+1][r-1]  # transition formula
                if array[l][r] and r-l+1>maximum:
                    start=l
                    maximum=r-l+1
        return s[start:start+maximum]



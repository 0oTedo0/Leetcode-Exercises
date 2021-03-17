class Solution:
    def convert(self, s, numRows):
        if numRows==1:return s
        ans=[]
        n=len(s)
        cycle=2*numRows-2
        for i in range(numRows):
            j=i
            while(j<n):
                ans.append(s[j])
                if i!=0 and i!=numRows-1 and j+cycle-2*i<n:  # rows are visited twice except for the first and the last row
                    ans.append(s[j+cycle-2*i])
                j+=cycle

        return ''.join(ans)

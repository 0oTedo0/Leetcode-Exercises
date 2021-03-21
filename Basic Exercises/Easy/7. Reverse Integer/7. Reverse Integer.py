class Solution:
    def reverse(self, x: int) -> int:
        flag=-1 if x<0 else 1
        x*=flag
        ans=0
        while(x):
            if not -2**31<=ans<=2**31-1:
                return 0
            ans=10*ans+x%10
            x//=10
        ans*=flag
        return ans if -2**31<=ans<=2**31-1 else 0

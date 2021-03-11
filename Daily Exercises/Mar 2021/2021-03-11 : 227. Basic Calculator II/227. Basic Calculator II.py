class Solution:
    def calculate(self, s):
        stk=list()
        preSign = '+'
        num = 0
        n = len(s)
        for i in range(n):
            if '0'<=s[i]<='9':
                num=num*10+int(s[i])
            if (not ('0'<=s[i]<='9')) and s[i]!=' ' or i==n-1:  # deal with the operation only when it comes to an operation or the last digit
                if preSign=='+':
                    stk.append(num)
                elif preSign=='-':
                    stk.append(-num)
                elif preSign=='*':
                    stk[-1]*=num
                elif preSign=='/':
                    stk[-1]=int(stk[-1]/num)  # note that we should round it to zero since some numbers are negative
                preSign=s[i]
                num=0
        return sum(stk)

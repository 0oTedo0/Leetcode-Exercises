class Solution:
    def calculate(self, s):
        ops=[1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while (i < n):
            if s[i] == ' ':
                i+=1
            elif s[i] == '+':
                sign = ops[-1]
                i+=1
            elif s[i] == '-':
                sign = -ops[-1]
                i+=1
            elif s[i] == '(':
                ops.append(sign)
                i+=1
            elif s[i] == ')':
                ops.pop()
                i+=1
            else:
                num = 0
                while (i < n and '0' <= s[i] <= '9'):
                    num = num * 10 + int(s[i])
                    i+=1
                ret += sign * num
            
        return ret

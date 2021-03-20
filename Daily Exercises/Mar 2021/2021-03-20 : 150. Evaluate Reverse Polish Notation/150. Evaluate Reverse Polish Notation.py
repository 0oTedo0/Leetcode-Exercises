class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=list()
        for item in tokens:
            if item=="+":
                result=s[-2]+s[-1]
            elif item=="-":
                result=s[-2]-s[-1]
            elif item=="*":
                result=s[-2]*s[-1]
            elif item=="/":
                result=int(s[-2]/s[-1])
            else:
                s.append(int(item))
                continue
            s.pop()
            s.pop()
            s.append(result)
        return s[0]

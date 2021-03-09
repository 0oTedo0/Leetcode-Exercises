class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=list()  # use list as a stack
        for item in S:
            if stack and stack[-1]==item:
                stack.pop()  # cancel it out
            else:
                stack.append(item)
        return ''.join(stack)

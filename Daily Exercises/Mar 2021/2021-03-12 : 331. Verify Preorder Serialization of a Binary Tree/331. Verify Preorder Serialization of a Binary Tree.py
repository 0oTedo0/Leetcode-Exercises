class Solution:
    def isValidSerialization(self, preorder):
        stack=list()
        elements=preorder.split(",")  # get every element
        for item in elements:
            stack.append(item)
            while(len(stack)>2 and stack[-1]=="#" and stack[-2]=="#"):  # if there are two '#' on the top of the stack, pop them and change the new top element to '#'
                stack.pop()
                stack.pop()
                if stack[-1]=="#":  # it disobeys the tree pre-order
                    return False
                stack[-1]="#"

        if len(stack)==1 and stack[0]=="#":  # it is valid only when the remaining element is '#'
            return True
        else:
            return False

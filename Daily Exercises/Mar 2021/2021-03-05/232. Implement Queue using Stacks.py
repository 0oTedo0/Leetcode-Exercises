class MyQueue:

    def __init__(self):
      """Initialization"""
        self.s1=list()  # Input stack
        self.s2=list()  # Output stack

    def push(self, x):
        self.s1.append(x)  # Push to input stack

    def pop(self):
        if(not len(self.s2)):  # If output stack is empty
            while(self.s1):
                self.s2.append(self.s1.pop())  # Fill output stack with input stack
        return self.s2.pop()  # Pop from output stack

    def peek(self):
        if(not len(self.s2)):  # If output stack is empty
            while(self.s1):
                self.s2.append(self.s1.pop())  # Fill output stack with input stack
        return self.s2[-1]

    def empty(self):
        return not (len(self.s1) or len(self.s2))

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

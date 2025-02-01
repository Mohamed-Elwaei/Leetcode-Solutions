class MyQueue(object):

    def __init__(self):
        self.s1=[]
    # def shuffle(self):
    #     if not self.s1:
    #         while self.s2:
    #             self.s1.append(self.s2.pop())
    #     elif not self.s2:
    #         while self.s1:
    #             self.s2.append(self.s1.pop())

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)  

        

    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[0]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.s1:
            return True
        return False    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
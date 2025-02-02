"""
We can do all operations in O(1) by using extra memory.

If we call inc(k,val), then we have to increment st[0], st[1], ... st[n-1].

When we pop an element from the stack.
We return st[last] + add[st.size]

We then have to add add[st.size] to add[st.size-1] and set add[st.size] = 0.


"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.n = n = maxSize

        self.st = []
        self.add = [0] * n
        
        
    def push(self, x: int) -> None:
        st = self.st
        n = self.n
        if len(st) < n:
            st.append(x)

    def pop(self) -> int:
        st = self.st
        if len(st) == 0:
            return -1
        n = len(st) - 1

        ret = st.pop() + self.add[n]
        if n > 0:
            self.add[n-1] += self.add[n]
        self.add[n] = 0

        return ret


    def increment(self, k: int, val: int) -> None:

        n = len(self.st)
        k = min(k, n) - 1
        if k >= 0:
            self.add[k] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
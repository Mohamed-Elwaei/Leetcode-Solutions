class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:

        st = []
        n = str(n)
        flag = 0
        for c in n:
            if not st or st[-1] <= int(c):
                st.append(int(c))
            else:
                flag = 1
                break
        #Original number = 567732
        #Stack after the for loop will be 566999

        if flag == False: return int(n)
        st[-1] -= 1
        while len(st) >= 2 and st[-1] < st[-2]:
            st.pop()
            st[-1] -= 1

        if len(st) == 1 and st[-1] == 0:
                return int('9' * (len(n) - 1)) 
             
        st.extend(['9'] * (len(n) - len(st)))
        st = [str(c) for c in st]
        st = int(''.join(st))
        return st
        
def minFlips( a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans=0
        for i in range(33):
            C=(c>>i) & 1
            B=(b>>i) & 1
            A=(a>>i) & 1

            if C==A|B: #No changes
                continue
            elif C:
                ans+=1
            elif A&B:
                ans+=2
            else:
                ans+=1
        return ans



#a 0010 
#b 0110
#c 0101
print(minFlips(2,6,5))
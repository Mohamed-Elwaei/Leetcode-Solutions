def hasAlternatingBits( n):
        """
        :type n: int
        :rtype: bool
        """
        four=4
        if n%2:
            n=n>>1

        while n:
            if n&-n!=2:
                 return False
            n>>=2
        return True


print(hasAlternatingBits(7))
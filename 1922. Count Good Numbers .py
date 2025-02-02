from math import ceil,floor
def binpow(a,b):
    if b==0:
        return 1
    res=binpow(a,b//2)

    if b%2==1:
        return (res*res*a)%((10**9)+7)
    else:
        return (res*res)%((10**9)+7)
        
def countGoodNumbers( n):
    """
    :type n: int
    :rtype: int
    """

    if n%2==0:
            return ((binpow(5,n//2))*binpow(4,n//2))%((10**9)+7)
    return ((binpow(5,(n+1)//2))*binpow(4,(n-1)//2))%((10**9)+7)


print(countGoodNumbers(1))
def getSum( a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """

    ans=0
    carry=0

    if a<0 and b<0 :
        ans^=-1
        ans&=(ans+1)

    for i in range(0,11):
        bita=(a>>i) & 1
        bitb=(b>>i) & 1

        currbit=bita^bitb^carry
        carry=(bita&bitb) | (bita&carry) | (bitb&carry)
        ans+=((currbit)<<i)

    if carry:
        ans^=-1
        ans|=1
    return ans



print(getSum(-8,-12))
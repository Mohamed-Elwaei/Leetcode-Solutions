def binaryGap( n):
    """
    :type n: int
    :rtype: int
    """
    ones=0
    lastbit=0
    maxDist=0
    for i in range(33):
        bit=(n>>i) &1
        if bit:
            ones+=1
            maxDist=max(maxDist, i-lastbit)
            lastbit=i
    
    if ones>1:
        return maxDist
    return 0

print(binaryGap(12))

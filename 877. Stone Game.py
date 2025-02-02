class Solution(object):
    
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        total = sum(piles)


        alice,bob = 0,0
        l=0
        r= len(piles)-1
        turn = 1

        while r>l:
            curr = 0
            if piles[l ] == piles[r]:
                p=l+1
                q=r-1

                while q>p and piles[q]!=piles[p]:
                    q+=1
                    p-=1
                if piles[q]<piles[p]:
                    curr = piles[r]
                    r-=1
                else:
                    curr = piles[l]
                    l+=1
            
            if piles[r]>piles[l]:
                curr = piles[r]
                r-=1
            else:
                curr = piles[l]
                l+=1
            
            if turn:
                alice+=curr
            else:
                bob+=curr
            
            if alice>total//2:
                return True
            if bob>total//2:
                return False


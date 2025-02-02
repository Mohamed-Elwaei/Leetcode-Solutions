class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people) - 1
        count = currWeight = 0
        while l <= r:
            boat = 0
            while l <= r and people[r] + currWeight <= limit and boat < 2:
                currWeight += people[r]
                r -= 1
                boat +=1

            while l <= r and people[l] + currWeight <= limit and boat < 2:
                currWeight += people[l]
                l += 1
                boat +=1
            count += 1
            currWeight = 0
        return count


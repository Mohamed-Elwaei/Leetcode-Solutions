class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def bs(house):
            l,r = 0,len(heaters) - 1
            closest = heaters[0]
            while l <= r:
                mid = l + (r - l) // 2
                if heaters[mid] - house > 0:
                    r = mid - 1
                elif heaters[mid] - house < 0:
                    l = mid + 1
                else:
                    return heaters[mid]
                if abs(heaters[mid] - house) < abs(closest - house):
                    closest = heaters[mid]
            return closest

        ans = 0
        for house in houses:
            closest = bs(house)
            ans = max(ans, abs(closest - house))
        return ans
            
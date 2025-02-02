class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def condition(mid):
            balls = m - 1
            lastPosition = position[0]

            for p in position[1:]:
                if p - lastPosition >= mid:
                    balls -= 1
                    lastPosition = p
                if balls == 0:
                    return True
            return balls == 0


        position.sort()
        l,r = 0, position[-1] - position[0]


        while l <= r:
            mid = (r - l)//2 + l

            if condition(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
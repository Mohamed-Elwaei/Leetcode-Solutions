class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        


        counter = {}
        n = len(fruits)
        l = 0

        ans = 0
        for r in range(n):
            counter[fruits[r]] = counter.get(fruits[r],0) + 1
            while len(counter) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                l += 1

            ans = max(ans, r - l + 1)
        return ans
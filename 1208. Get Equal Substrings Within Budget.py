class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def bs(target):
            l,r = 0,len(prefixSum) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if prefixSum[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        prefixSum = [abs(ord(a) - ord(b)) for a,b in zip(s,t)]
        for i in range(1, len(prefixSum)):
            prefixSum[i] += prefixSum[i - 1]
        ret = 0
        print(prefixSum)
        for i, n in enumerate(prefixSum):
            if n <= maxCost:
                ret = max(ret, i + 1)
            else:
                ret = max(ret, i - bs(n - maxCost))
            print(ret, n)
        return ret
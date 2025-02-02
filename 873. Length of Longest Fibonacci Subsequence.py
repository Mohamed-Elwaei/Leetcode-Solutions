class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        

        # a,b = 1,1
        # tmp=a+b
        # while tmp<100:
        #     print(tmp)
        #     b  = a
        #     a  = tmp
        #     tmp = a+b
        A = arr
        s = set(A)
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b, l = A[i], A[j], 2
                while a + b in s:
                    a, b, l = b, a + b, l + 1
                res = max(res, l)
        return res if res > 2 else 0
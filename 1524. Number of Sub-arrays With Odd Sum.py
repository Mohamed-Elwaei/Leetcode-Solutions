class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        #1 <= N <= 10^5
        #1 <= arr[i] <= 100

        #An odd number is the result of odd no. - even no.
        #If we encounter an odd no. See how many even no.s occur before it.
        #If we encounter an even no. See how many odd no.s occur before it.
        #Use a prefix Sum. PrefixSum[i] = sum(arr[0..i])
        #If prefixSum[i] is even: see how many odd prefixSums occur before it.
        #If prefixSum[i] is odd: see how many even prefixSums occur before it.

        #arr = [1,3,5]
        #ps = [1,4,9]
        # 1 + 1 + 2 = 4
        #arr = [2,4,6]
        #ps = [2,6,12]

        M = 10**9 + 7
        N = len(arr)
        prefixSum = 0
        odd, even = 0, 1
        answer = 0
        for i in range(N):
            prefixSum += arr[i]
            if prefixSum % 2 == 0:
                answer = (answer + odd) % M
            elif prefixSum % 2 == 1:
                answer = (answer + even) % M
            odd += prefixSum % 2 == 1
            even += prefixSum % 2 == 0
        return answer

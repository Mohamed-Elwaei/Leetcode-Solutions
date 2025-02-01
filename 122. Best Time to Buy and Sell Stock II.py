"""
I think we can solve it in Constant memory.


One thing we shoulf not is if arr[i] < arr[i+1] < .... arr[j].
The we only need to keep track of arr[i] and arr[j].



We will partition the array into strictly increasing subarrays.
We then will add the last - first element from each subarray to the answer.


"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = max_ = prices[0]

        answer = 0
        for p in prices[1:]:
            if p < max_:
                answer += max_ - min_
                min_ = max_ = p
            else:
                max_ = p
        
        answer += max_ - min_
        return answer
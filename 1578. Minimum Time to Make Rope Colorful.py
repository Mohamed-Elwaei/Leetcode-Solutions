"""
Solution would be partition the array into subarrays of consecutive colors.


For each group:
    let the size of the group be G.

    we pick the G-1 least costly ballons. and leave the most expensive.

We can do this in one pass with no extra memory.
"""

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        last = '' #last is the letter in the group
        sum_ = 0 #sum of the costs of the current group
        largest = 0 #largest time needed for a ballon in the group.
        answer = 0

        for balloon, time in zip(colors, neededTime):
            if balloon != last:
                answer += (sum_ - largest)

                last = balloon
                sum_ = largest = time
            else:
                sum_ += time
                largest = max(time, largest)

        answer += (sum_ - largest)

        return answer



        
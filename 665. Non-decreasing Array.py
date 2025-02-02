class Solution:
    def checkPossibility(self, array: List[int]) -> bool:
        modified_nums = 0


        for i in range(len(array) - 1):
            if array[i] <= array[i + 1]:
                continue
            
            #Which element should we change? Left or Right.

            #Here we would need to change the left element.
            if i == 0 or array[i + 1] >= array[i - 1]:
                array[i] = array[i - 1]
            elif array[i + 1] < array[i - 1]:
                array[i + 1] = array[i]
            modified_nums += 1
        return modified_nums <= 1
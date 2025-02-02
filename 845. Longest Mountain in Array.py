class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        #[2,1,4,7,3,2,5]
        #inc = 2
        #dec = 2

        # mountain = inc + dec + 1
        #[2,7,9,1,2,3,4,5,4,3,2,1]
        #inc = 4
        #dec = 4

        inc = dec = 0
        N = len(arr)
        answer = 0
        for i in range(N - 1):
            if arr[i] < arr[i + 1]:
                if dec > 0:  
                    inc = 0
                inc += 1 
                dec = 0
            elif arr[i] > arr[i + 1]:
                if inc > 0:
                    dec += 1
            else:
                inc = dec = 0
            if inc>0 and dec>0 and inc + dec + 1 >= 3:
                answer = max(answer, inc + dec + 1)
        return answer
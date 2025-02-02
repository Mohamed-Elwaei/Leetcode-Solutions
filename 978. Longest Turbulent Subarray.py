class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i = 0
        ans = 0
        while i < len(arr):
            turn = None
            j = i+1
            while j < len(arr):
                

                if arr[j]<arr[j-1]:
                    if turn == None or turn =='inc':
                        turn = 'dec'
                    else:
                        break
                        
                elif arr[j]>arr[j-1]:
                    if turn == None or turn =='dec':
                        turn = 'inc'
                    else:
                        break
                else:
                    break
                j+=1
                
            ans = max(ans,j-i)

            i = max(j-1,i+1)
        return ans
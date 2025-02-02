# The Solution class contains a method to find the sum of minimums of all subarrays in a given array.
class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)  # Get the length of the input array
        left = [-1] * n  # Store the index of previous less element for each element in the array
        right = [n] * n  # Store the index of next less element for each element in the array
        stack = []  # Initialize an empty stack for indices

        # Calculate the previous less element for each element in the array
        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:  # Ensure that the top of the stack is < current element value
                stack.pop()  # Pop elements from stack while the current element is smaller or equal
            if stack:
                left[i] = stack[-1]  # Update left index if stack is not empty
            stack.append(i)  # Push the current index onto the stack

        stack = []  # Reset the stack for the next loop

        # Calculate the next less element for each element in the array, going backwards
        for i in range(n - 1, -1, -1):  # Start from end of the array and move backwards
            while stack and arr[stack[-1]] > arr[i]:  # Similar stack operation but with strict inequality
                stack.pop()  # Pop elements while current element is smaller
            if stack:
                right[i] = stack[-1]  # Update right index if stack is not empty
            stack.append(i)  # Push current index to the stack

        mod = 10**9 + 7  # Define modulus for the final result

        # Calculate the sum of all minimum subarray values with their respective frequencies
        # The frequency is the product of the lengths of subarrays to the left and right
        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
      
        return result  # Return the result sum, modulo 10^9 + 7
    


s = Solution()

print(s.sumSubarrayMins(arr = [3,1,2,4]))

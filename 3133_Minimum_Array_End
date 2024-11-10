class Solution(object):
    def minEnd(self, n, x):  # Define the method with parameters
        a = []  # Initialize an empty array
        k = 1   # Start with shift of 1
        
        # Start the array with the first element as `x`
        a.append(x)
        
        # Loop until we have `n` elements in the array
        while len(a) < n:
            # Start with the smallest candidate greater than the last element in `a`
            result = a[-1] + 1
            
            # Find the next number that maintains the AND condition
            while (result & x) != x:
                result += 1
            
            # Add the valid result to the array
            a.append(result)
        
        return a[-1]  # Return the last element in the array

# Example usage
n = 3
x = 4
solution = Solution()
print(solution.minEnd(n, x))  # Expected output is 6

class Solution:
    def find_longest_common_pattern(self, a, b):
        min_length = min(len(a), len(b))
        max_len = max(len(a), len(b))
        matching = ""
        
        # Iterate over each possible starting position in `b`
        for k in range(min_length):
            p = k  # Start from each position in `b`
            current_match = ""  # Temporary string to store the current match

            # Traverse the longer string `a` to find matching characters
            for i in range(max_len):
                if p < min_length and a[i] == b[p]:  # Compare character at `a[i]` and `b[p]`
                    current_match += a[i]
                    p += 1  # Move to the next character in `b`
                else:
                    p = k  # Reset `p` to the start position in `b`
                    break  # Break if there's no match to start fresh in the next outer loop iteration

            # Update `matching` with the longest pattern found so far
            if len(current_match) > len(matching):
                matching = current_match

        return matching

# Example usage
s1 = "ABBABCABAB"
s2 = "ABC"

solution = Solution()
print(solution.find_longest_common_pattern(s1, s2))  # Expected output: "AB"

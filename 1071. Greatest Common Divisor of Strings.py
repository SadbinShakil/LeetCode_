class Solution:
    def find_longest_common_pattern(self, a, b):
        min_length = min(len(a), len(b))
        max_len = max(len(a), len(b))
        matching = ""
        
        for k in range(len(a)):
            current_match = ""
            p = 0  # Always start from the beginning of `b` for each new starting position in `a`

            for i in range(k, max_len):
                # Make sure we stay within bounds for both `a` and `b`
                if p < min_length and a[i] == b[p]:  # Compare character at `a[i]` and `b[p]`
                    current_match += a[i]
                    p += 1  # Move to the next character in `b`
                else:
                    break  # Break if there's no match

            # Update `matching` with the longest pattern found so far
            if len(current_match) > len(matching):
                matching = current_match

        return matching

# Example usage
s1 = "ABABABAB"
s2 = "BAB"

solution = Solution()
print(solution.find_longest_common_pattern(s1, s2))  # Expected output: "BAB"

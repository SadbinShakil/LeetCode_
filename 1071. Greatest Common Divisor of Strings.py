class Solution:

    def find_longest_common_pattern(self, a, b):
        min_length = min(len(a), len(b))
        max_len    = max(len(a), len(b))
        matching = ""
        for k in range(min_length):
          for i in range(max_len):
            if(a[i] == b[k]):
              if a[i] not in matching:
                matching += a[i]
                k = k + 1 if k + 1 < min_length else 0
              else:
                k = 0
              
        return matching

# Example usage
s1 = "ABBABCABAB"
s2 = "ABC"

solution = Solution()
print(solution.find_longest_common_pattern(s1, s2))


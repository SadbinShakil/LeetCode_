
# Custom zip_longest function to handle unequal lengths
def zip_longest(s1, s2, fillvalue=''):
    max_len = max(len(s1), len(s2))
    return [(s1[i] if i < len(s1) else fillvalue, s2[i] if i < len(s2) else fillvalue) for i in range(max_len)]


class Solution(object):
    def mergeAlternately(self, word1, word2):
      return ''.join((i or '') + (j or '') for i, j in zip_longest(word1, word2))


word1 = "abcqqwr"
word2 = "pqrs"
solution = Solution()
print(solution.mergeAlternately(word1, word2))
      
        

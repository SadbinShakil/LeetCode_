class Solution(object):
    def maxVowels(self, s, k):
      count = 0
      vowel_count = 0
      max_count = 0
      vowels = ['a', 'e', 'i', 'o', 'u']
      start_index = 0
      
      if len(s) == 1:
        if s in vowels:
          return 1
        else:
          return 0

      for i in range(k):
        if s[i] in vowels:
          vowel_count+=1
          max_count = vowel_count

      for i in range(k, len(s)):
        if s[i] in vowels:
          vowel_count+=1
        if s[start_index] in vowels:
          vowel_count-=1
        start_index+=1
        if vowel_count > max_count:
          max_count = vowel_count
      return max_count




s = "leetcode"
k = 3
solution = Solution()
solution.maxVowels(s, k)

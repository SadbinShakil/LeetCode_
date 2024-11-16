class Solution(object):
    def reverseVowels(self, s):
      s = list(s)
      vowels_got = []
      positions = []
      vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
      for i in range(len(s)):
        if s[i] in vowels:
          vowels_got.append(s[i])
          positions.append(i)
      positions.reverse()
      j = 0
      for position in positions:
        s[position] = vowels_got[j]
        j+=1
      return "".join(s)


s = "IceCreAm"
solution = Solution()
solution.reverseVowels(s)


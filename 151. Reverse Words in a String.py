class Solution(object):
    def reverseWords(self, s):
      temp1 = []
      a = []
      for i in range(len(s)):
        if s[i] != " ":
          a.append(s[i])
        elif s[i] == " ":
          temp1.append("".join(a))
          a = []
      temp1.append("".join(a))
      temp1.reverse()
      temp1 = " ".join(temp1)
      temp1 = temp1.split()

      temp1 = " ".join(temp1)
      return [temp1]

s = "  Bob    Loves    Alice  "
solution = Solution()
solution.reverseWords(s)

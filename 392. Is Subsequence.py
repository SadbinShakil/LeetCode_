class Solution(object):
  def isSubsequence(self, s, t):
    p = 0
    count = 0
    if (s == t):
      return True
    if (len(s) == 0 and len(t) == 0):
      return True
    if (len(s) == 0 and len(t) != 0):
      return True
    if (len(s) != 0 and len(t) == 0):
      return False
    if (len(s) > len(t)):
      return False

    for i in range(len(t)):
      if p<len(s):
        if(t[i] == s[p]):
          p+=1
          count+=1
        if(count == len(s)):
          return True
    return False
    
s = "b"
t = "abc"
solution = Solution()
solution.isSubsequence(s, t)

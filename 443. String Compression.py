import json
class Solution(object):
  def compress(self, chars):
    p1 = None
    p2 = 0
    write = 0
    for char in chars:
      if p1 is None:
        p1 = char
        p2+=1
      elif char == p1:
        p2+=1
        # print(char)
        # print(p2)
      elif char != p1:
        chars[write] = str(p1)
        write+=1
        if p2>1:
          for digit in str(p2):
            chars[write] = str(digit)
            write+=1
        p1 = char
        p2 = 1
    chars[write] = str(p1)
    write+=1
    if p2>1:
      for digit in str(p2):
        chars[write] = str(digit)
        write+=1
    return write


chars = ["a","a","b","b","c","c","c","d","d","e","e","e","e","e","e","e","e","e","e"]
solution = Solution()
length = solution.compress(chars)
print(chars[:length])

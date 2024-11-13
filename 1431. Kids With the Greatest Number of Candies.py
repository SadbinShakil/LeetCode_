class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
      output = []
      for kids in candies:
        if kids + extraCandies >= max(candies):
          print(True)
          output.append(True)
        else:
          print(False)
          output.append(False)
      return output

candies = [2,3,5,1,3]
extraCandies = 3
solution = Solution()
solution.kidsWithCandies(candies, extraCandies)

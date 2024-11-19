#Not optimized
class Solution(object):
    def productExceptSelf(self, nums):
      temp = []
      x = 1
      for item in nums:
        for i in range(len(nums)):
          if i != nums.index(item):
            x = x * nums[i]
        temp.append(x)
        x = 1
      return temp

nums = [-1,1,0,-3,3]
solution = Solution()
solution.productExceptSelf(nums)


#Optimized
class Solution(object):

  def suff(self, nums):
      temp = []
      x = 1
      for i in range(len(nums)-1, -1, -1):  # Iterate backward
          temp.append(x)  # Append the current suffix product
          x = x * nums[i]  # Update suffix product for the next iteration
      temp.reverse()  # Reverse the list to match the correct order
      return temp


  def priff(self, nums):
    temp1 = []
    x = 1
    for i in range(len(nums)):
        temp1.append(x)
        x = x * nums[i]
    return temp1

  def productExceptSelf(self, nums):
    q = self.suff(nums)
    r = self.priff(nums)
    result = []
    for a, b in zip(q, r):  # Iterate through both lists simultaneously
      result.append(a * b)      # Multiply corresponding elements
    return result

nums = [1,2,3,4]
solution = Solution()
solution.productExceptSelf(nums)





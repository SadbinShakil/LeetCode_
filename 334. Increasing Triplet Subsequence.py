#If not consecutive
class Solution(object):
    def increasingTriplet(self, nums):
      n1 = float('inf')
      n2 = float('inf')
      if len(nums) < 3:
        return False

      if len(nums) == 3:
        if nums[0] < nums[1] and nums[1] < nums[2]:
          return True
        else:
          return False

      for i in range(len(nums)):
        if n1 != float('inf') and n2 != float('inf'):
          if nums[i]>n2:
            return True
        if nums[i]<=n1:
          n1 = nums[i]
        else:
          n2 = nums[i]
      return False


nums = [12,0,3]
solution = Solution()
solution.increasingTriplet(nums)

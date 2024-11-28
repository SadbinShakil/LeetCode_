
class Solution(object):
    def moveZeroes(self, nums):
      position = 0
      for i in range(len(nums)):
        if nums[i] == 0:
          position +=1
        elif nums[i] != 0 and position>0:
          nums[i-position] = nums[i]
          nums[i] = 0
          

      return nums
          
nums = [0,0,1,0,0,0,0,0,3,0,0,12,0,0,15]
solution = Solution()
solution.moveZeroes(nums)

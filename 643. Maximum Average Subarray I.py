class Solution(object):
    def findMaxAverage(self, nums, k):
      curr_sum = 0
      curr_avg = float('inf')
      max_avg = float('inf')
      start_index = 0

      if len(nums) == 1:
        return nums[0]

      if len(nums) == 0:
        return 0



      for i in range(k):
        curr_sum += nums[i]
      curr_avg = curr_sum/float(k)
      max_avg = curr_avg

      for i in range(k, len(nums)):
        # print("in step ",i,"=", curr_sum, nums[k], nums[start_index])
        curr_sum = curr_sum + nums[i] - nums[start_index]
        start_index+=1
        curr_avg = curr_sum/float(k)
        if curr_avg > max_avg:
          max_avg = curr_avg
      return max_avg

nums = [1,12,-5,-6,50,3]
k = 4
solution = Solution()
solution.findMaxAverage(nums, k)

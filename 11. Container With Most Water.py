#optimized one with 2 pointers
class Solution(object):
  def maxArea(self, height):
    max_area = 0
    left = 0
    right = len(height)-1
    current_area = 0
    if len(height) == 1:
      return height[0]

    if len(height) == 0:
      return 0

    if len(height) == 2:
      return min(height[0], height[1])*1

    while(left < right):
      current_area = min(height[left], height[right])*(right-left)
      if current_area > max_area:
        max_area = current_area
      if (height[left] > height[right]):
        right-=1
      else:
        left+=1
    return max_area


height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
solution.maxArea(height)

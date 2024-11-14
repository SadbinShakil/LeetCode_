class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
      temp = 0
      for space in range(len(flowerbed)):
        if flowerbed[space] == 0:
          if space == 0:
            if len(flowerbed)>1 and flowerbed[space + 1] == 0:
              flowerbed[space] = 1
              if temp<n:
                temp += 1
              else:
                break
            elif len(flowerbed)==1:
              flowerbed[space] = 1
              if temp<n:
                temp += 1
              else:
                break
          elif space == len(flowerbed) - 1:
            if flowerbed[space - 1] == 0:
              flowerbed[space] = 1
              if temp<n:
                temp += 1
              else:
                break
          
          elif flowerbed[space - 1] == 0 and flowerbed[space + 1] == 0:
              flowerbed[space] = 1
              if temp<n:
                temp += 1
              else:
                break
      if temp >= n:
        return True
      else:
        return False

flowerbed = [1,0,0,0,1]
n = 1
solution = Solution()
solution.canPlaceFlowers(flowerbed, n)
            
        

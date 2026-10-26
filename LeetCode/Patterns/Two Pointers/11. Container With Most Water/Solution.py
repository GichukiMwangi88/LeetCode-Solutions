class Solution:
    def maxArea(self, height: list[int]) -> int:
      # initialize the pointers
      left = 0
      right = len(height) - 1
      max_area = 0

      # Traverse the list
      while left < right:
        width = right - left

        min_height = min(height[left], height[right])

        current_area = min_height * width

        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1


      return max_area

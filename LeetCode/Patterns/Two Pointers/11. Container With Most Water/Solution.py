class Solution:
    def maxArea(self, height: list[int]) -> int:
      # initialize the pointers
      left = 0
      right = len(height) - 1
      max_area = 0

      # Traverse the list
      while left < right:
        # Calculate the width
        width = right - left

        # Find the min height because the shorter height limits
        # how much water the container can hold
        min_height = min(height[left], height[right])

        current_area = min_height * width

        # Keeps track of the largest area found
        max_area = max(max_area, current_area)

        # Move the pointer to the shorter height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1


      return max_area

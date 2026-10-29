class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = curr_sum = sum(nums[:k]) # Sum 4 elements a time

        for i in range(len(nums) - k):
            curr_sum += nums[i + k] - nums[i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum / k


        
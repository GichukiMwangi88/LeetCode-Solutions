class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
        Declare first and second val
        Iterate nums array
        First Condition: if nums[i] < first --> update first to be nums[i]
        Second Condition: if nums[i] < second --> update second to be nums[i]
        If the above are all true, then return True, since we have a triplet
        subsequence that satisfies both conditions:
            - i < j < k and nums[i] < nums[j] < nums[k]
        """
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
        
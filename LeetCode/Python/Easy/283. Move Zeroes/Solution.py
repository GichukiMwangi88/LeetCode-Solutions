class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Use an insert var to keep track of the zeroes
        [0,1,0,3,12]
         i          
        Iterate the nums array
        When we encounter a non-zero element, we swap with i,
        then increment i, move it to the next position
        1st Iteration
        [1,0,0,3,12]
           i (new position of i), look for the next non-zero element
        2nd Iteration
        [1,3,0,0,12]
             i
        """
        insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1

        
        
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Build the prefix and postfix arrays
        prefix = [1] * len(nums)  # prefill the list with 1s [1,1,1,1]
        # Populate the prefix list
        for i in range(1,len(nums)):
            # [1,2,3,4]
            # Prefix --> [1,1,2,6]
            prefix[i] = prefix[i - 1] * nums[i- 1]
        print(prefix)

        # Prefix list
        postfix = [1] * len(nums) # [1,1,1,1]
        # Populate the posftfix list
        for i in range(len(nums) - 2, -1, -1):
            # [1,2,3,4]
            # Postfix --> [24,12,4,1]
            postfix[i] = postfix[i + 1] * nums[i + 1]

        print(postfix)

        result = [1] * len(nums)
        print(result)

        # Combine both arrays
        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]

        print(result)

        return result


        
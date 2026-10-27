from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Declare an empty default dict
        d = defaultdict(int)
        # print("Dictionary:", d)
        pairs = 0

        for num in nums:
            complement = k - num
            if d[complement] > 0:
                d[complement] -= 1
                pairs += 1
            else:
                d[num] += 1


        # print("Dictionary: ", d)

        return pairs
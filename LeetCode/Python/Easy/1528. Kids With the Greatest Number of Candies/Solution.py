class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Find the largest value in the list
        # Ex, candies = [2,3,5,1,3], extraCandies = 3
        largestVal = max(candies) # largestVal = 5

        result = [] # boolean result array []

        for candy in candies:
            # 1st iteration: if 2 + 3 >= 5  ---> add true to result
            if candy + extraCandies >= largestVal:
                result.append(True)
            else:
                result.append(False)

        return result




        
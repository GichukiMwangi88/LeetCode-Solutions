class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """
        Base Case: if n == 0, return True
        Rule --> Left = 0   Current = 0   Right = 0
        if true, can plant flower, decrement n then repeat
        """

        # Base case, n == 0, return True
        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            left = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed) - 1) or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1  # Plant flower w/o violating adj rule
                n -= 1
                if n == 0:
                    return True
        return False
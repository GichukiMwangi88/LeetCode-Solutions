class Solution:
    def reverseVowels(self, s: str) -> str:
        # Strings are immutable, therefore convert s into a list
        s = list(s)
        # Create a set of vowels
        vowels = {"a","e","i","o","u", "A","E","I","O","U"}
        # Left and Right pointers to keep track of vowels in list
        left, right = 0, len(s) - 1

        
        # Loop until the left and right pointers meet in the middle
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left] # Swap the vowels found at left and right positions
                left += 1
                right -= 1
        # Convert the list to a string   
        return ''.join(s)

        
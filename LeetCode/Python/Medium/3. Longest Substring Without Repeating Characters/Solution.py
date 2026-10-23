class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       # Dictionary to store char and its corresponding index
        # Dictionary used to track characters
        # char --> most recent index
        """
            {
                'a': 3,
                'b': 4,
                'c': 5
            }
        """
        seen = {}
        # Left pointer, marks the beginning of current window
        l = 0
        # Variable to store the longest valid substring found so far
        maxLength = 0

        # Iterate the string s
        for r, char in enumerate(s): # Enumerate gives us both index, r and character char.
            # Add the first char to the seen dict with the corresponding index as its value
            char = s[r]
            # Check if current char, where the R pointer is, is in dict
            # and if the char's index is > than the L pointer index
            # Checking for duplicates here, move the L pointer index
            # = previousDuplicate index + 1
            # Second condition ensures L doesn't move backwards
            if char in seen:
                # Update the L pointer to move past the duplicate's previous index + 1
                l = max(l, seen[char] + 1)

            # Store the most recent position of the current character
            seen[char] = r

            # Calculate the current window length (r - l +1), 
            # +1 need since we are including both ends, r & l
            # Compare the current window length(maxLength) with the longest window seen so far
            maxLength = max(maxLength, r - l + 1)

        return maxLength
        
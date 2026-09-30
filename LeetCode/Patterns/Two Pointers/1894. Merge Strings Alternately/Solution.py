class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Create an empty array to hold the result
        result = []
        """
        Determine the minimum length of the shorter string
        in order to alternate characters from both strings 
        up to that point, the last letter of the shorter string
        """
        min_len = min(len(word1), len(word2))

        # Iterate and add to result arr alternating
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])

        # Handle cases where word1 or word2 is longer,
        # Just append the longer word chars to the result
        if len(word1) > len(word2):
            result.append(word1[min_len:])
        result.append(word2[min_len:])

        return "".join(result)
        
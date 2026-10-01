import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        When both strings are combined, either way, they should 
        be equal. If not, return a blank string
        Checks for repeating pattern
        Eg. "ABCABC" + "ABC" = "ABCABCABC"
            "ABC" + "ABCABC" = "ABCABCABC"

        Eg 2. "LEET" + "CODE" = "LEETCODE"
              "CODE" + "LEET" = "CODELEET"
              ... No repeating pattern here

        """
        if str1 + str2 != str2 + str1:
            return ""

        # Find the common length of the string to be returned
        gcd = math.gcd(len(str1), len(str2))

        if len(str1) > len(str2):
            return str1[:gcd]
        return str2[:gcd]

        
        
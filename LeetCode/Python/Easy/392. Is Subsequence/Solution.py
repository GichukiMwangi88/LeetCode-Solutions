class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize two pointers for s and t
        ptr_s = ptr_t = 0

        # Iterate both strings checking if all letters in s are in t
        while ptr_s < len(s) and ptr_t < len(t):
            # Check if the two pointers point to the same letter
            if s[ptr_s] == t[ptr_t]:
                # Advance the s pointer to the next letter in s
                ptr_s += 1
            # Keep advancing t pointer by 1 regardless
            ptr_t += 1

        # Return True if ptr_s reaches the end of string s,
        # O'wise return False
        return ptr_s >= len(s)


        
        
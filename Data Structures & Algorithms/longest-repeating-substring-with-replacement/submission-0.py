class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window = {}
        total = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0) # or initilize if it is zero. 
            while r-l+1 - max(window.values()) > k:
                window[s[l]]-=1
                l += 1
            total = max(total, (r-l+1))
        return total

    


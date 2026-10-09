class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        total = 0 
        for r in range(0,len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            if len(window)>total:
                total = len(window)

        return total

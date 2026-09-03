class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_clean = ""
        for i in s:
            if i.isalnum():
                s_clean+=i.lower()

        curr=0
        end = len(s_clean)-1
        while curr < end:
            if s_clean[curr] != s_clean[end]:
                return False
            curr +=1
            end -=1
        return True

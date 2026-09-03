class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_list = ""
        s=s.lower()
        s_clean = ""
        for i in s:
            if i.isalnum():
                new_list = new_list + i
                s_clean = i + s_clean
        if s_clean == new_list:
            return True
        return False